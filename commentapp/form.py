from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content','image'] # 사용자에게 입력받을 것
        labels = {
            'content':'comment'
        }