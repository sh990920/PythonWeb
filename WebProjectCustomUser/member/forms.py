from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("memberId", "password", "nickname", "like_category")

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()

class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("memberId", "password")