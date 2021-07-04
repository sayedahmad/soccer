from django import forms
from player.models import Player
from match.models import Match

class MatchPlayersForm(forms.Form):
    """ Form shows list of players  """
    players=Player.objects.all()
    player = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple, required=True, queryset=players)


class DateInput(forms.DateInput):
    """ date input type"""
    input_type = 'date'

class MatchMakerForm(forms.ModelForm):
    """ form shows suggested match with selected players and teams with players strength"""
    class Meta:
        model= Match
        fields="__all__"
        widgets = {
            'match_date': DateInput()
        }