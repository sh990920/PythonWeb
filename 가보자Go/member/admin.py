from django.contrib import admin
from .models import Member


@admin.register(Member)
class UserAdmin(admin.ModelAdmin):
    list_display = ("memberId",)  # 관리자 페이지에서 보일 필드를 지정
    exclude = ("password",)  # 사용자 상세 정보에서 비밀번호 필드를 노출하지 않음
