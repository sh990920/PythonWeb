from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 채팅 메인 페이지
def main(request):
    return render(request, "chat/index.html")

def chatroom(request, mettingPK, memberPK):
    chatting = Chat.objects.filter(mettingIdx=mettingPK)
    form = ChatForm()
    return render(request, "chat/chatroom.html", {"chatList" : chatting, "memberPK" : memberPK, "mettingPK" : mettingPK, "form" : form})

@csrf_exempt
def chatting(request):
    if request.method == "GET":
        chat = ChatForm(request.GET)
        mettingPK = request.GET.get("mettingIdx", None)
        memberPk = request.GET.get("memberIdx", None)
        if chat.is_valid():
            todo = chat.save(commit=False)
            todo.save()
    return redirect("/chat/chatroom/" + str(mettingPK) + "/" + str(memberPk) + "/")