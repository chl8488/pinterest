from django.forms import ModelForm
from ProfileApp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','message','nickname']
