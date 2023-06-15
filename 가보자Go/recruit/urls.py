from django.urls import path
from . import views

# recruit 앱에서 사용하는 url 정의
urlpatterns = [
    # 동행글 리스트 페이지
    path("", views.recruitMain),
    # 동행글 상세보기
    path("post/", views.recruitPost),
    # 동행글 작성하기 페이지
    path("write/", views.recruitWritePage),
    # 동행글 작성하기
    path("write/write/", views.recruitWrite),
    # 동행글 수정하기
    path("", views.recruitModifyPage),
]