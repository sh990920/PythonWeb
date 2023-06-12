from typing import Any, Dict
from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# Create your views here.
# FBV 방식
# def index(request):
#     posts = Post.objects.all().order_by("-pk")
#     return render(request, "blog/index.html", {"posts":posts})

# CBV 방식
class PostList(ListView):
    model = Post
    # template_name = "blog/index.html"
    ordering = "-pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["categories"] = Category.objects.all() # 모든 카테고리 데이터를 가져와 categories 키에 저장
        context["no_category_post_count"] = Post.objects.filter(
            category=None
        ).count() # 카테고리가 지정되지 않은 포스트의 개수를 저장
        return context

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, "blog/single_post_page.html", {"post":post})

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["categories"] = Category.objects.all() # 모든 카테고리 데이터를 가져와 categories 키에 저장
        context["no_category_post_count"] = Post.objects.filter(
            category=None
        ).count() # 카테고리가 지정되지 않은 포스트의 개수를 저장
        return context

def category_page(request, slug):
    if slug == "no_category":
        category = "미분류"
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        "blog/post_list.html",
        {
            "post_list" : post_list,
            "categories" : Category.objects.all(),
            "no_category_post_count" : Post.objects.filter(category=None).count(),
            "category" : category,
        }
    )