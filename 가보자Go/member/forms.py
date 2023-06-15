from django import forms
from .models import Member

# 회원가입을 진행하기위한 폼 생성
class SignUpForm(forms.ModelForm):
    class Meta:
        # 사용자 클래스로 모델 생성
        model = Member
        # 모델을 생성할 때 들어갈 필드 지정
        fields = ("memberId", "password", "nickname", "like_category")

    # 사용자를 저장하기 위한 함수
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()


# 로그인을 진행하기위한 폼 생성
class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("memberId", "password")
