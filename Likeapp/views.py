from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from Likeapp.models import LikeRecord

@transaction.atomic
def db_transaction(user, article):
    article.like += 1
    article.save()

    if LikeRecord.objects.filter(user=user, article=article).exists():
        raise ValidationError('Like already exists')
        # return HttpResponseRedirect(
        #     reverse('article:detail', kwargs={'pk': article.pk})
        # )
    else:
        LikeRecord(user=user, article=article).save()



@method_decorator(login_required,'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        #  self.request.GET.get('like_pk'),{'pk': kwargs['pk']}
        return reverse('article:detail', kwargs={'pk': kwargs['pk']})

    # pk=self.request.GET.get('like_pk'), pk=kwargs['pk']
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        user = self.request.user

        try:
            db_transaction(user, article)
            messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')
        except ValidationError:
            messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다!')
            return HttpResponseRedirect(
                reverse('article:detail', kwargs={'pk': kwargs['pk']})
            )

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)


