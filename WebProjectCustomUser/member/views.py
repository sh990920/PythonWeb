from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.views.decorators.csrf import csrf_exempt
from .forms import MemberForm, LoginForm
from django.contrib.auth import login, logout, authenticate

# 메인 페이지
def main(request):
    return render(request, "member/main.html")


# 회원가입 페이지로 이동
def sign_up_form(request):
    return render(request, "member/signUp.html")

# 아이디 체크
def idCheck(request):
    result = "no"
    if request.method == "GET":
        checkMemberId = request.GET.get("memberId", None)
        # admin 계정이면 결과값이 없다고 나옴
        try:
            member = Member.objects.get(memberId = checkMemberId)
        except:
            result = "yes"
    return HttpResponse(result)

# 닉네임 체크
def nicknameCheck(request):
    result = "no"
    if request.method == "GET":
        checkNickname = request.GET.get("nickname", None)
        try:
            member = Member.objects.get(nickname = checkNickname)
        except:
            result = "yes"
    return HttpResponse(result)

# 회원가입
@csrf_exempt
def signUp(request):
    result = "no"
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            result = "yes"
            member = form.save()
            # member.save()
    return HttpResponse(result)

# 로그인 페이지
def loginForm(request):
    form = LoginForm()
    return render(request, "member/login.html", {"form" : form})

# 로그인 기능
@csrf_exempt
def user_login(request):
    result = "no"
    if request.method == "POST":
        checkMemberId = request.POST.get("memberId", None)
        checkPassword = request.POST.get("password", None)
        print(checkMemberId, checkPassword)
        account = authenticate(request, username=checkMemberId, password=checkPassword)
        print(account)
        if account is not None:
            print("로그인 기능 성공")
            login(request, account)
            result = "yes"
    return HttpResponse(result)

# 로그아웃 기능
def user_logout(request):
    logout(request)
    return redirect("/")
