from django.db import models
from django.db.models import Sum, F

from match.models import Match

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
   

    @property
    def ranking(self):
        host_matches = self.host_team.all()
        guest_matches = self.guest_team.all()
        rank = 0
        host_matche_scores =0
        guest_matche_scores =0

        if len(host_matches)>0:
            for match in host_matches:
                host_matche_scores += match.host_status
        if len(guest_matches)>0:
            for match in guest_matches:
                guest_matche_scores += match.guest_status
        if len(host_matches)+len(guest_matches)>0:
            rank=(host_matche_scores+guest_matche_scores)/(len(host_matches)+len(guest_matches))
        
        return rank
    
    @property
    def total_matches(self):
     
        return self.host_team.count()+self.guest_team.count()
    
    @property
    def total_win(self):
        total=0

        for match in self.host_team.all():
            if match.host_status==2:
                total+=1
        for match in self.guest_team.all():
            if match.guest_status==2:
                total+=1
        return total
    
    @property
    def total_Draw(self):
        total=0

        for match in self.host_team.all():
            if match.host_status==1:
                total+=1
        for match in self.guest_team.all():
            if match.guest_status==1:
                total+=1
        return total

    @property
    def total_lost(self):
        total=0

        for match in self.host_team.all():
            if match.host_status==0:
                total+=1
        for match in self.guest_team.all():
            if match.guest_status==0:
                total+=1
        return total

    @property
    def total_marks(self):
        total=0

        for match in self.host_team.all():
            total+=match.host_status
        for match in self.guest_team.all():
            total+=match.guest_status
        return total
    
        
    def __str__(self):
        return self.name
