from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm
from django.views.decorators.csrf import csrf_exempt
from member.models import Member

# 채팅 메인 페이지 - 나중에 동행글 생기면 그쪽으로 url, 함수 변경 예정
def main(request):
    return render(request, "chat/index.html")

# 채팅방으로 이동하는 함수
# 파라미터로 mettingPK 와 memberPK 를 받아온다
def chatroom(request, mettingPK, memberPK):
    # 동행글 idx로 채팅 데이터베이스에서 원하는 데이터만 추출
    chatting = Chat.objects.filter(mettingIdx=mettingPK)

    # 멤버 객체를 가져와서 채팅에서 본인이 친 채팅인지 구분하기 위해 객체 생성
    member = Member.objects.get(id=memberPK)
    
    # 채팅을 보내기 위한 폼 태그 생성
    form = ChatForm()
    
    # 채팅 기록과 사용자 idx, 동행글 idx, 폼태그를 전달
    return render(
        request,
        "chat/chatroom.html",
        {
            "chatList": chatting,       # 채팅 리스트
            "memberPK": memberPK,       # 멤버 pk(사실 username)
            "mettingPK": mettingPK,     # 만남글 pk
            "form": form,               # 채팅을 저장하기위한 form
            "memberId" : member,        # 멤버 객체(username과 비교하기 위해 member 객체를 가져감)
        },
    )


# csrf 토큰값을 사용하지 않음
@csrf_exempt
# 채팅 내용을 저장하기위한 함수
def chatting(request):
    
    # request method 가 GET 인지 확인
    if request.method == "GET":
        
        # method 가 GET 이라면 채팅폼으로 request 내용 전달
        chat = ChatForm(request.GET)
        
        # mettingPK 와 memberPK 를 다시 저장(채팅방 페이지로 보내기위해 사용)
        mettingPK = request.GET.get("mettingIdx", None)
        memberPk = request.GET.get("memberIdx", None)
        
        # 채팅 객체에 이상이 있는지 확인
        if chat.is_valid():
            
            # 폼태그 저장 이후 데이터 반환
            chatData = chat.save(commit=False)
            
            # 반환된 데이터를 데이터베이스에 저장
            chatData.save()
    
    # 데이터를 저장시킨 이후 채팅방 페이지로 다시 이동
    return redirect("/chat/chatroom/" + str(mettingPK) + "/" + str(memberPk) + "/")
