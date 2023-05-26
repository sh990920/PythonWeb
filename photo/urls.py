# 프로젝트 전체에 관한 url은 myweb/urls.py가 관리하고
# photo앱에 대한 url은 photo폴더 안에 있는 urls.py가 관리

from django.urls import path
from . import views

urlpatterns = [
    path("", views.photo_list, name = "photo_list"),
    # <int:pk> : pk라는 이름이 정수형 변수가 들어갈 자리라는 의미
    path("photo/<int:pk>/", views.photo_detail, name="photo_detail"),
    path("photo/new/", views.photo_post, name="photo_post"),
    path("photo/<int:pk>/edit/", views.photo_edit, name="photo_adit")
]
