from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import PlayerRegisterationForm
from .models import Player
# Create your views here.


class PlayerRegisterationView(CreateView):
    
    """Player Registration View"""

    template_name = "player/register.html"
    success_url = reverse_lazy("player_list")
    model = Player
    fields = "__all__"


class PlayerListView(ListView):

    """List players """

    model = Player
    template_name = "player/list.html"
    context_object_name = 'players'
    paginate_by = 5


class PlayerDetailsView(DetailView):
    """ Details of a single player """
    model = Player
    template_name = 'player/detial.html'
    context_object_name = 'player'


class PlayerUpdateView(UpdateView):
    """Update a single player """

    model = Player
    template_name = 'player/update.html'
    context_object_name = 'player'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('player_detial', kwargs={'pk': self.object.id})


class PlayerDeleteView(DeleteView):
    """Update a single player """
    model = Player
    template_name = 'player/delete.html'
    success_url = reverse_lazy('player_list')
