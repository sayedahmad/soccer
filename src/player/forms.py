from django.forms import ModelForm
from.models import Player


class PlayerRegisterationForm(ModelForm):
    """ Form for Player registration""" 
    
    class Meta:
        model = Player
        fields = '__all__'
