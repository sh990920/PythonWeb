from django.db import models
from member.models import Member
from recruit.models import Recruit

# 채팅을 위한 Chat 객체 생성
class Chat(models.Model):
    # 글 idx - Recruit 의 id 를 참조하는 포린키 설정
    # on_delete=models.CASCADE : 참조하는 데이터가 사라지면 모든 열 삭제
    # db_column : 컬럼명을 직접 지정
    mettingIdx = models.ForeignKey(
        Recruit, on_delete=models.CASCADE, db_column="mettingIdx"
    )
    
    # 유저 idx - member 의 id 를 참조하는 포린키 설정
    memberIdx = models.ForeignKey(
        Member, on_delete=models.CASCADE, db_column="memberIdx"
    )

    # 내용
    # max_length : 최대 글자 수 설정
    content = models.CharField(max_length=200)
    
    # 작성시간
    # 시간과 날짜를 자동으로 입력
    # form 에서 따로 작성을 하지 않아도 되도록 blank=True 설정
    write_time = models.DateTimeField(auto_now_add=True, blank=True)
