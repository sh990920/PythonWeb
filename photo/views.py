from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo # 포토 객체 연결(java로 생각하면 Entity 객체와 연결하는 느낌)
from .forms import PhotoForm

# get_object_or_404() : 모델로부터 데이터를 찾아보고 만약 찾는 데이터가 없다면 404에러를 반환
## 찾는 데이터가 없는 경우에 대한 에러 처리를 Django가 알아서 할 수 있도록 함

# Create your views here.
def photo_list(request):
    # render를 사용해 photo/photo_list.html을 렌더링
    # 웹에 보여질 수 있도록 가공하여 전달
    photos = Photo.objects.all()
    # photo.objects.all() : photo 모델 데이터를 모두 가져오기
    # Jpa 의 repository.findAll() 과 같은느낌인거같다
    return render(request, "photo/photo_list.html", {"photos" : photos})
    # {"photos" : photos} : Spring-Boot 의 Model 바인딩과 같은 개념인거같음

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk = pk)
    return render(request, "photo/photo_detail.html", {"photo" : photo})

def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.save()
            return redirect("photo_detail", pk = photo.pk)
    else:
        form = PhotoForm()
    return render(request, "photo/photo_post.html", {"form" : form})

def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk = pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance = photo)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.save()
            return redirect("photo_detail", pk = photo.pk)
    else:
        form = PhotoForm(instance = photo)
    return render(request, "photo/photo_post.html", {"form" : form})
