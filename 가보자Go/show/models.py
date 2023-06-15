from django.db import models

# 공연 객체 생성
class Show(models.Model):
    # 공연 제목 : 길이 설정 해야함, notNull
    showTitle = models.CharField(max_length=200)

    # 공연 장르 : 길이 설정 해야함, notNull
    showCategory = models.CharField(max_length=200)

    # 공연 기간 : 길이 설정 해야함, notNull
    showPeriod = models.CharField(max_length=200)

    # 공연 시간 : 길이 설정 해야함, notNull
    showTime = models.CharField(max_length=200)

    # 공연 장소 : 길이 설정 해야함, notNull
    showPlace = models.CharField(max_length=200)

    # 연령대 : 길이 설정 해야함
    showAgeGroup = models.CharField(max_length=200, null=True)

    # 티켓가격 : notNull
    ticketPrice = models.IntegerField()

    # 출연진 : 길이 설정 해야함, notNull
    showCast = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.showTitle}"