from django.contrib import admin
from .models import Chat

# 관리자 페이지에서 확인할 수 있도록 등록
admin.site.register(Chat)
