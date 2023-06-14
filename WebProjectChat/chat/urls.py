from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("chatroom/<int:mettingPK>/<int:memberPK>/", views.chatroom, name="chatroom"),
    path("chatting/", views.chatting),
]