from django.shortcuts import render, redirect
from member.models import Member
from .models import Recruit
from .forms import RecruitForm

# Create your views here.
# 만들어야할 것들
# 1. 동행글 전체리스트 페이지
# 2. 동행글 상세보기 페이지
# 3. 동행글 작성 페이지
# 4. 동행글 수정 페이지

# 동행글 전체보기 페이지
def recruitMain(request):
    # 기능 개발 준비중
    recruitList = Recruit.objects.all()
    return render(request, "recruitMain/recruitMain.html", {"recruitList" : recruitList})

# 동행글 상세보기 페이지
def recruitPost(request):
    if request.method == "GET":
        user_pk = request.user.pk
        pk = request.GET.get("recruitPK")
        recruit = Recruit.objects.get(id=pk)
        member = Member.objects.get(id=recruit.returnMemberIdx().pk)
    return render(request, "recruitPost/recruitPost.html", {"recruit" : recruit, "member" : member ,"user_pk" : user_pk})

# 동행글 작성 페이지
def recruitWritePage(request):
    # 기능 개발 준비중
    # 유저가 로그인을 한 상태로 들어왔는지 확인
    if request.user.is_authenticated:
        # 로그인을 한 상태로 들어왔으면 유저 정보 받기
        member_user = request.user
        # 유저 정보를 받아서 Member 객체 찾기
        member = Member.objects.get(memberId=member_user)
        memberIdx = member.pk
        print(memberIdx)
        form = RecruitForm()
    return render(request, "recruitWrite/recruitWrite.html", {"memberIdx" : memberIdx, "form" : form})

# 동행글 작성
def recruitWrite(request):
    form = RecruitForm(request.GET)
    if form.is_valid():
        recruit = form.save(commit=False)
        recruit.save()
        return redirect("/recruit/")

# 동행글 수정 페이지
# 작성글과 같은 기능을 수행하기 때문에 같은 html을 쓸 예정
def recruitModifyPage(reqeust):
    # 기능 개발 준비중
    return render(reqeust, "recruitWrite/recruitWrite.html")
