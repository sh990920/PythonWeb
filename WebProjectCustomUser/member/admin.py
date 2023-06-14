from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class UserAdmin(admin.ModelAdmin):
    list_display = ('memberId',)
    exclude = ('password',)  # 사용자 상세 정보에서 비밀번호 필드를 노출하지 않음