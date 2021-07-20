from django.contrib.auth.forms import UserCreationForm

class AccountUserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 초기화 이후에 username의 값을 비활성화(
        # 이 한줄이 없으면 기본 UserCreationForm 과 다를게 없음)
        self.fields['username'].disabled = True