from django.shortcuts import render
from .models import Blog #같은 폴더안에 있는 models.py안에 있는 Blog 객체를 가져와라.

# Create your views here.

def home(request):
    blogs = Blog.objects    # model로부터 객체목록을 전달받음. 이런 전달받은 객체 목록을 '쿼리셋'이라고 함. '쿼리셋'을 받아 정렬하거나 기능들을 표시할 수 있는데 이를 '메소드'라고 함.
    return render(request, 'blog/home.html', {'blogs' : blogs})

    #쿼리셋과 메소드의 형식
    #모델.쿼리셋(objects).메소드

    #home.html에서 blogs.all()을 하면 blogs는 원래 Blog.objects를 의미하므로 모델.object(쿼리셋).all()(메소드)를 만족한 것. all() Blogs에서 만든 모든 객체를 다 가져와라.
    #.count() : 개수 반환 메소드, .first() : 첫 번째 객체를 반환해라, .rest() : 마지막 객체를 반환해라 등등 매우 많음.