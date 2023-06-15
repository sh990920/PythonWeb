from django.urls import path
from . import views

# show 앱에서 사용하는 url 정의
urlpatterns = [
    path("", views.show_board, name="board_list"),
    path("create/", views.create_post, name="create_post"),
    path("<int:pk>/", views.show_post_detail, name="show_post_detail"),
    path("<int:pk>/remove/", views.remove_post, name="remove_post"),
    path("<int:pk>/edit/", views.edit_post, name="edit_post"),
]