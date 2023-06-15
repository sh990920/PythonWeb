from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate

# 메인 페이지
def main(request):
    # 유저가 로그인을 한 상태인지 확인
    if request.user.is_authenticated:
        # 로그인을 했다면 메인페이지로 이동
        return render(request, "main/main.html")
    else:
        # 로그인을 하지 않았다면 /n 으로 로그인을 하지 않았다고 url에 전달
        return redirect("/n")


# 로그인을 하지 않은 메인페이지
def mainN(request):
    return render(request, "main/main.html")


# 회원가입 페이지로 이동
def sign_up_form(request):
    return render(request, "signUp/signUp.html")


# 아이디 체크
def idCheck(request):
    # 결과값을 no 로 지정
    result = "no"
    # request 의 method를 확인
    if request.method == "GET":
        # method가 GET 이라면 파라미터로 넘어온 memeberId 를 checkMemberId 변수에 저장
        # 만약 값이 없다면 None 이 변수에 저장
        checkMemberId = request.GET.get("memberId", None)
        # admin 계정은 검색 결과가 없다고 나옴
        try:
            # checkMemberId 변수에 저장된 값으로 데이터 조회
            # 값이 없으면 오류가 발생하기 때문에 오류처리를 필수로 진행해야함
            # 변수에 저장된 값으로 member 객체가 반환된다면
            # checkMemberId로 지정된 id가 있으므로 결과값을 수정하지 않음
            member = Member.objects.get(memberId=checkMemberId)
        except:
            # 오류가 발생했다면 객체를 찾지 못했으므로
            # checkMemberId로 지정된 id가 없으므로 결과값을 yes 로 수정
            result = "yes"
    # HttpResponse로 result 변수를 전달
    return HttpResponse(result)


# 닉네임 체크
# 함수 안의 내용은 아이디 체크와 동일
def nicknameCheck(request):
    result = "no"
    if request.method == "GET":
        checkNickname = request.GET.get("nickname", None)
        try:
            member = Member.objects.get(nickname=checkNickname)
        except:
            result = "yes"
    return HttpResponse(result)


# 회원가입
# csrf_exempt 데코레이터를 사용해서 csrf 토큰값을 조회하지 않음
@csrf_exempt
# 하지만 보안성에서 취약할 수 있으므로 나중에 수정해야함
def signUp(request):
    # 결과값을 no 로 지정
    result = "no"
    # request의 method가 POST 인지 확인
    if request.method == "POST":
        # method 가 POST 가 맞다면 파라미터로 받아온 값들을
        # Form 클래스를 사용해서 model 생성
        form = SignUpForm(request.POST)
        # form 객체에 이상이 있는지 확인
        if form.is_valid():
            # 이상이 없다면 데이터베이스에 저장
            member = form.save()
            # 데이터베이스 저장 이후 결과값을 yes로 지정
            result = "yes"
    # HttpResponse 로 result 변수값을 전달
    return HttpResponse(result)


# 로그인 페이지
def loginForm(request):
    # LoginForm 을 사용해서 폼태그 사용하기
    form = LoginForm()
    return render(request, "login/login.html", {"form": form})


# 로그인 기능
@csrf_exempt
def user_login(request):
    # 결과값을 no로 지정
    result = "no"
    # request 의 method가 POST 인지 확인
    if request.method == "POST":
        # request 로 넘어온 파라미터 중 memberId 값 을 checkMemberId 변수에 저장
        # 만약 값이 없다면 None 저장
        checkMemberId = request.POST.get("memberId", None)
        # request 로 넘어온 파라미터 중 password 값 을 checkPassword 변수에 저장
        # 만약 값이 없다면 None 저장
        checkPassword = request.POST.get("password", None)
        # authenticate 를 사용해서 account 생성
        # 파라미터로 request, username, password 가 필요함
        # username : 로그인을 진행 할 사용자 id
        # password : 로그인을 진행 할 사용자 비밀번호
        account = authenticate(request, username=checkMemberId, password=checkPassword)
        # account 변수에 값이 정상적으로 들어있는지 확인
        print(account)
        if account is not None:
            print("test")
            # account 변수와 request 로 로그인 하기
            login(request, account)
            # 로그인이 정상적으로 진행되었다면 result 를 yes 로 지정
            result = "yes"
    # HttpResponse 를 사용해서 result 값 반환
    return HttpResponse(result)


# 로그아웃 기능
def user_logout(request):
    # 로그인읉 통해 생성된 세션 삭제
    logout(request)
    # 로그아웃을 진행한 이후 메인 페이지로 이동
    return redirect("/")


# 마이페이지
def my_page(request):
    # 유저가 로그인을 한 상태로 들어왔는지 확인
    if request.user.is_authenticated:
        # 로그인을 한 상태로 들어왔으면 유저 정보 받기
        member_user = request.user
        # 유저 정보를 받아서 Member 객체 찾기
        member = Member.objects.get(memberId=member_user)
        # member 객체가 찾아졌다면 렌더링을 통해 myPage 에 member 객체 함께 보내기
        return render(request, "myPage/myPage.html", {"member": member})
    else:
        return redirect("/n")


# 정보 수정 기능
def updateMember(request):
    # 아직 개발중
    return render(request, "")
