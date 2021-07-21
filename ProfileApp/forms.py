from django.forms import ModelForm
from ProfileApp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','message','nickname']
        labels = {
            'message':'자신을 소개해보세요',
            'nickname':'닉네임',
        }
