from django.db import models

# Create your models here.
class Chat(models.Model):
    # 글 idx
    mettingIdx = models.IntegerField()
    # 유저 idx
    memberIdx = models.IntegerField()
    # 내용
    content = models.CharField(max_length=200)
    # 작성시간
    write_time = models.DateTimeField(auto_now_add=True, blank=True) # 시간과 날짜를 자동으로 입력