from django import forms
from .models import Recruit

# 동행글을 데이터베이스에 저장하기 위한 폼 생성
class RecruitForm(forms.ModelForm):
    class Meta:
        # Recruit 객체로 모델 생성
        model = Recruit
        # 데이터베이스에 저장될 필드 선언
        fields = ("recruitTitle", "recruitContent", "showIdx", "memberIdx")