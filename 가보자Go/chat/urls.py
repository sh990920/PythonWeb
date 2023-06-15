from django.urls import path
from . import views

# chat 앱에서 사용하는 url 정의
urlpatterns = [
    # 채팅 메인페이지(나중에 동행 앱이 생성되면 위치 변경 예정)
    path("", views.main),
    
    # 채팅방에 들어가기위한 url
    # meetingPK 로 동행글 idx를 받아옴
    # memberPK 로 사용자 idx를 받아옴
    path("chatroom/<int:mettingPK>/<int:memberPK>/", views.chatroom, name="chatroom"),
    
    # 채팅 처리를 위한 url
    path("chatting/", views.chatting),
]
