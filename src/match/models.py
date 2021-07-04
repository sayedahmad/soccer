from django.db import models
from player.models import Player
from functools import partial
from django import forms
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
# Create your models here.


class Match(models.Model):
    """ Match model that includes host, guest teams with thier respected playrs, scores for both team and match date """
    host_team = models.ForeignKey(
        "team.Team", on_delete=models.CASCADE, related_name="host_team", null=True, blank=True)
    host_team_players = models.ManyToManyField(
        'player.Player', related_name='host_team_player')
    guest_team = models.ForeignKey(
        "team.Team", on_delete=models.CASCADE, related_name="guest_team", null=True, blank=True)
    guest_team_players = models.ManyToManyField(
        'player.Player', related_name='guest_team_player')
    host_team_score = models.IntegerField(null=True, blank=True)
    guest_team_score = models.IntegerField(null=True, blank=True)
    match_date = models.DateField(null=True)

    @property
    def host_status(self):
        """host team: returns 2 for match win, 1 for draw 0 fro lost """
        result=0
        if self.host_team_score>self.guest_team_score:
            result=2
        elif self.host_team_score==self.guest_team_score:
            result=1
        
        return result


    @property
    def guest_status(self):
        """guest team: returns 2 for match win, 1 for draw 0 fro lost """
        result=0
        if self.host_team_score<self.guest_team_score:
            result=2
        elif self.host_team_score==self.guest_team_score:
            result=1
        
        return result
    
    
    def __str__(self):
        return f"{self.host_team} vs {self.guest_team}"
