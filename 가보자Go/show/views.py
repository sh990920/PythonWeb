from django.shortcuts import render, redirect
from .models import Show
from .forms import CreatePostForm
from django.core.paginator import Paginator

# Create your views here.
def show_board(request):
    page = request.GET.get("page")
    show_list = Show.objects.all().order_by("-pk")
    paginator = Paginator(show_list, 5)
    posts = paginator.get_page(page)
    context = {
        "page" : posts,
    }
    return render(request, "show/show_board.html", context)

def show_post_detail(request, pk):
    post = Show.objects.get(id=pk)
    return render(request, "show/show_post_detail.html", {"post" : post})

def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            create_post = form.save(commit=False)
            create_post.save()
            return redirect("board_list")
    else:
        form=CreatePostForm()
    context={"form" : form}
    return render(request, "show/create_post.html", context)

def remove_post(request, pk):
    post = Show.objects.get(pk=pk)
    post.delete()
    return redirect("board_list")

def edit_post(request, pk):
    post = Show.objects.get(id=pk)
    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("board_list")
    else:
        form = CreatePostForm(instance=post)
        return render(request, "show/create_post.html", {"form" : form})