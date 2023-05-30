from django.db import models
# todo 모델
# title : 제목
# description : Todo에 대한 설명
# created : Todo 생성 일자
# complete : Todo 완료 여부
# important : Todo 중요 여부

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) # 빈칸 허용
    created = models.DateTimeField(auto_now_add=True) # 시간과 날짜를 집어넣지 않으면 자동으로 현재 날짜 입력
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title