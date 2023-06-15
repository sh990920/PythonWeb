# 커스텀유저 기능을 사용하기 위해서 필요한 모듈 임포트
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# 유저를 생성할 때 사용할 헬퍼 클래스
# AbstractBaseUser가 참고하니, 그보다 위에 작성되어야 한다.
# 인수로 받는 email 등을 다른 것으로 바꿀 수 있다.
# 다음 코드는 email 대신 memberId를 넣는 등 메뉴얼에서 제공하는 코드를 바꾸어 사용할 수 있다.
class UserManager(BaseUserManager):
    # 일반 사용지 생성을 위한 메서드
    # 아래의 유저 클래스에서 생성한 컬럼들을 사용해서 일반 유저를 만드는 메서드
    # memberId : 로그인을 위한 id
    # password : 로그인을 위한 비밀번호
    # nickname : 사용자 닉네임
    # like_category : 좋아하는 장르(1개만 저장 가능)
    # profile : 사용자 프로필사진(처음엔 사진을 넣어주지않음) - 이후 나중에 사용자 상세페이지에서 변경 가능
    def create_user(self, memberId, password, nickname, like_category, profile=None):
        # 이 안에 유저 정보에 필요한 필드를 넣으면 된다.
        # 왼쪽이 필드값, 오른쪽이 파라미터로 받아온 변수값
        user = self.model(
            memberId=memberId,
            nickname=nickname,
            like_category=like_category,
            profile=profile,
        )
        # 비밀번호 암호화
        user.set_password(password)
        # 생성한 사용자를 데이터베이스에 저장
        user.save(using=self._db)
        # 저장한 유저 반환
        return user

    # 관리자 계정을 생성하는 메서드
    # 관리자 계정에서 사용할 컬럼만 넣어서 사용
    # memberId : 관리자 id
    # password : 관리자 비밀번호
    # nickname : 관리자 닉네임
    def create_superuser(self, memberId, password, nickname):
        # 이 안에 관리자 정보에 필요한 필드를 넣으면 된다.
        user = self.create_user(
            memberId,
            password=password,
            nickname=nickname,
            like_category=None,
            profile=None,
        )
        # 관리자 권한을 지정
        user.is_admin = True
        # 생성한 관리자를 데이터베이스에 저장
        user.save(using=self._db)
        # 저장한 관리자 반환
        return user


# 커스텀 유저 모델. 다음 코드도 최대한 단순화 한 것이지만... 필수 필드를 갖고 있다.
# is_active : 계정을 활성화 하는가.
# is_admin : 관리자 계정인가.

# 필수인듯 필수 아닌 기타 필드
# 꼭 정의되지 않아도 되지만, 정의되지 않으면 admin 페이지 접속 자체가 안된다.

# is_staff	어드민에 접속할 권한.

# 커스텀 유저 모델을 생성하기 위해서 AbstractBaseUser를 상속받아 사용한다.
class Member(AbstractBaseUser):
    memberId = models.CharField(max_length=20, unique=True)  # 유저ID
    password = models.CharField(max_length=200)  # 유저 PW
    nickname = models.CharField(max_length=20, unique=True)  # 유저 닉네임
    like_category = models.CharField(
        max_length=20, default=None, blank=True, null=True
    )  # 좋아하는 공연 분야
    profile = models.ImageField(
        upload_to="member/images/%Y/%m/%d/", blank=True, default=None, null=True
    )  # 유저 프로필사진
    is_active = models.BooleanField(default=True)  # 계정 활성화
    is_staff = models.BooleanField(default=False)  # 어드민에 접속할 권한
    is_admin = models.BooleanField(default=False)  # 관리자 권한

    objects = UserManager()  # 회원가입을 다룰 클래스를 지정

    USERNAME_FIELD = "memberId"  # 식별자로 사용할 필드
    REQUIRED_FIELDS = [  # 회원가입 때 필수 입력필드
        "password",
        "nickname",
    ]

    def __str__(self):
        return self.memberId

    def has_perm(self, perm, obj=None):
        # 권한 소지여부를 판단하기 위한 메서드
        return True

    def has_module_perms(self, app_label):
        # 앱 라벨을 받아, 해당 앱에 접근 가능한지 파악
        return True

    @property
    def is_staff(self):
        # 이게 True면 관리자화면에 접근 가능
        return self.is_admin
