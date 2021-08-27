from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from ProfileApp.decorators import profile_ownership_required
from ProfileApp.forms import ProfileCreationForm
from ProfileApp.models import Profile



class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'ProfileApp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        messages.add_message(self.request,messages.SUCCESS,'프로필이 생성되었습니다.')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})

@method_decorator(profile_ownership_required,'get')
@method_decorator(profile_ownership_required,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'ProfileApp/update.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, '프로필이 변경되었습니다.')
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})