from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import When, Case, F, IntegerField
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.urls import reverse_lazy, reverse
from .models import Match
from team.models import Team
from .forms import *

# Create your views here.


class MatchRegisterationView(CreateView):

    template_name = "match/register.html"
    success_url = reverse_lazy("match_list")
    model = Match
    form_class = MatchMakerForm


class MatchListView(ListView):
    """views matchs"""
    model = Match
    template_name = "match/list.html"
    context_object_name = 'matchs'
    # paginate_by = 5


class MatchDetailsView(DetailView):
    """show single match"""
    model = Match
    template_name = 'match/detial.html'
    context_object_name = 'match'


class MatchUpdateView(UpdateView):
    """update a single match"""
    model = Match
    template_name = 'match/update.html'
    context_object_name = 'match'
    form_class = MatchMakerForm

    def get_success_url(self):
        return reverse_lazy('match_detial', kwargs={'pk': self.object.id})


class MatchDeleteView(DeleteView):
    """ Deletes a single match object """
    model = Match
    template_name = 'match/delete.html'
    success_url = reverse_lazy('match_list')


class MatchMakerView(View):
    """ divide selected player in
     to two teams and propose teams with near samilar strengths """

    def get(self, request, *args, **kwargs):
        form = MatchPlayersForm()
        context = {
            'form': form,
        }

        if 'player' in request.GET:
            """ if players are requested and their number are at least two. divide them in two teams and pass them to find_players_team function """

            players = request.GET.getlist('player')
            if len(players) > 1:

                middle_index = int(len(players)//2)
                first_team_players_ids = players[:middle_index]
                second_team_players_ids = players[middle_index:]
                result = self.find_players_team(
                    first_team_players_ids, second_team_players_ids)
                match_maker_form = MatchMakerForm(initial={
                    'host_team': result['teams'][0],
                    'guest_team': result['teams'][1],
                    'host_team_players': result['players'][0],
                    'guest_team_players': result['players'][1],

                }
                )
                context = {
                    'teams': result['teams'],
                    'players': result['players'],
                    'form': match_maker_form
                }

                return render(request, "match/matchmakerregister.html", context)

        return render(request, "match/matchmakerview.html", context)

    def post(self, *args, **kwargs):
        """ Register suggested match with match registeration view """
        MatchRegisterationView.as_view()(self.request, kwargs)
        return redirect('match_list')

    def find_players_team(self, first_team_players_ids, second_team_players_ids):
        """ Receives player ids in two teams, calcualte the average players ranking in each team and find the samilar teams """
        first_team_ranking = 0
        second_team_ranking = 0
        first_team_players = []
        second_team_players = []

        for player_id in first_team_players_ids:
            """ Find the average Ranking of the players"""

            player = Player.objects.get(pk=int(player_id))
            first_team_players.append(player)
            first_team_ranking += player.ranking

        first_team_ranking /= len(first_team_players_ids)

        # second team
        for player_id in second_team_players_ids:
            """ Find the average Ranking of the players"""

            player = Player.objects.get(pk=int(player_id))
            second_team_players.append(player)
            second_team_ranking += player.ranking

        second_team_ranking /= len(second_team_players_ids)

        teams = Team.objects.all()
        # find teams with samilar strengths
        teams_ranking = [team.ranking for team in teams]
        first_team = min(range(len(teams_ranking)), key=lambda i: abs(
            teams_ranking[i]-first_team_ranking))
        second_team = min(range(len(teams_ranking)), key=lambda i: abs(
            teams_ranking[i]-second_team_ranking))

        return {'teams': [teams[first_team], teams[second_team]], 'players': [first_team_players, second_team_players]}
