from django.db import models
from member.models import Member

# 동행글
class Recruit(models.Model):
    # 글 제목
    recruitTitle = models.CharField(max_length=50)
    
    # 글 내용
    recruitContent = models.CharField(max_length=200)
    
    # 공연 idx
    showIdx = models.IntegerField()
    
    # 유저 idx - member 의 id 를 참조하는 포린키 설정
    # on_delete=models.CASCADE : 참조하는 데이터가 사라지면 모든 열 삭제
    # db_column : 컬럼명을 직접 지정
    memberIdx = models.ForeignKey(
        Member, on_delete=models.CASCADE, db_column="memberIdx"
    )

    def returnMemberIdx(this):
        return this.memberIdx
    