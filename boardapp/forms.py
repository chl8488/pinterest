from django.forms import ModelForm

from boardapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image','title','description']