from django.http import HttpResponseForbidden
from ProfileApp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # 우리가 요청을 받으면서 pk로 받은값을 가지고 있는 유저객체가 user가 됨
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
# 이런식으로 하면 우리가 게시나 포스트나 뭐든간에 받을때마다 그 pk를 확인해서
# 그 유저객체가 실제로 request를 보는 유저와 같은지 아닌지를 확인하고 아니라면 
# Forbidden으로 403 오류페이지를 보여주게 함