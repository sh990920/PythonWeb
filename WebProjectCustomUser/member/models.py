# 모델과 유저 모델을 임포트함
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# 유저를 생성할 때 사용할 헬퍼 클래스
# AbstractBaseUser가 참고하니, 그보다 위에 작성되어야 한다.
# 인수로 받는 email 등을 다른 것으로 바꿀 수 있다.
# 다음 코드는 email 대신 identifier를 넣는 등 메뉴얼에서 제공하는 코드를 바꾸어,
# 최대한 단순화하여 아이디와 패스워드만 받는 코드이다.
class UserManager(BaseUserManager):
    def create_user(self, memberId, password, nickname, like_category, profile=None):
        user = self.model(              # 이 안에 유저 정보에 필요한 필드를 넣으면 된다.
            memberId = memberId,    # 왼쪽이 필드, 오른쪽이 넣을 값.
            nickname = nickname,
            like_category = like_category,
            profile = profile,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, memberId, password, nickname):
        user = self.create_user(
            memberId,
            password=password,
            nickname = nickname,
            like_category=None,
            profile=None,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# 커스텀 유저 모델. 다음 코드도 최대한 단순화 한 것이지만... 필수 필드를 갖고 있다.
# is_active : 계정을 활성화 하는가.
# is_admin : 관리자 계정인가.

# 필수인듯 필수 아닌 기타 필드
# 꼭 정의되지 않아도 되지만, 정의되지 않으면 admin 페이지 접속 자체가 안된다.

# is_staff	어드민에 접속할 권한.

class Member(AbstractBaseUser):
    memberId = models.CharField(max_length=20, unique=True)                                                 # 유저ID
    password = models.CharField(max_length=200)                                                             # 유저 PW
    nickname = models.CharField(max_length=20, unique=True)                                                 # 유저 닉네임
    like_category = models.CharField(max_length=20, default=None, blank=True, null=True)                    # 좋아하는 공연 분야
    profile = models.ImageField(upload_to="member/images/%Y/%m/%d/", blank=True, default=None, null=True)   # 유저 프로필사진
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()  # 회원가입을 다룰 클래스를 지정한다.

    USERNAME_FIELD = 'memberId'   # 식별자로 사용할 필드.
    REQUIRED_FIELDS = [
        'password',
        'nickname',
    ] # 회원가입 때 필수 입력필드.

    def __str__(self):
        return self.memberId

    def has_perm(self, perm, obj=None):
        '''권한 소지여부를 판단하기 위한 메서드'''
        return True

    def has_module_perms(self, app_label):
        '''앱 라벨을 받아, 해당 앱에 접근 가능한지 파악'''
        return True

    @property
    def is_staff(self):
        '''이게 True면  관리자화면에 접근 가능'''
        return self.is_admin