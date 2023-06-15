from django.contrib import admin
from django.urls import path, include
from member import views as memberView

# 사용할 url 지정
urlpatterns = [
    # 관리자 페이지
    path("admin/", admin.site.urls),
    # 메인 페이지
    path("", memberView.main),
    # 아직 로그인을 하지않은 메인 페이지
    path("n/", memberView.mainN),
    # 회원가입, 로그인 등 member 앱을 쓰는 것들을 위한 url들
    path("member/", include("member.urls")),
    # 채팅 앱 안의 url을 사용
    path("chat/", include("chat.urls")),
    # 동행글 앱 안의 url을 사용
    path("recruit/", include("recruit.urls")),
    # 공연 앱 안의 url을 사용
    path("show/", include("show.urls")),
]
