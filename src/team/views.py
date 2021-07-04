from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Team
# Create your views here.


class TeamRegisterationView(CreateView):

    template_name = "team/register.html"
    success_url = reverse_lazy("team_list")
    model = Team
    fields = "__all__"


class TeamListView(ListView):
    model = Team
    template_name = "team/list.html"
    context_object_name = 'teams'

    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        team_ranks = [rank.ranking for rank in Team.objects.all()]
        context['team_lables'] = list(
            Team.objects.all().values_list('name', flat=True))
        context['team_rank'] = [rank.ranking for rank in Team.objects.all()]
    
        return context
    


class TeamDetailsView(DetailView):
    model = Team
    template_name = 'team/detial.html'
    context_object_name = 'team'


    


class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'team/update.html'
    context_object_name = 'team'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('team_detial', kwargs={'pk': self.object.id})


class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'team/delete.html'
    success_url = reverse_lazy('team_list')
