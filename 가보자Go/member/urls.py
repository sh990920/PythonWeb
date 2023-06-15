from django.urls import path
from . import views

urlpatterns = [
    # 회원가입 페이지로 이동
    path("signUpForm/", views.sign_up_form),
    # 아이디 체크 URL
    path("idCheck/", views.idCheck),
    # 닉네임 체크 URL
    path("nicknameCheck/", views.nicknameCheck),
    # 회원가입
    path("signUp/", views.signUp),
    # 로그인 페이지로 이동
    path("loginForm/", views.loginForm),
    # 로그인
    path("login/", views.user_login),
    # 로그아웃
    path("logout/", views.user_logout),
    # 마이페이지
    path("myPage/", views.my_page),
]
