from django import forms
from .models import Chat

# 채팅을 데이터베이스에 저장하기 위한 폼 생성
class ChatForm(forms.ModelForm):
    class Meta:
        # Chat 객체로 모델 생성
        model = Chat
        # 데이터베이스에 저장될 필드 선언
        fields = ("mettingIdx", "memberIdx", "content")
