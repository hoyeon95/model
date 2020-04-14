from django.contrib import admin
from .models import Blog #같은 폴더안에 있는 models.py안에 있는 Blog 객체를 가져와라.

admin.site.register(Blog) # admin 사이트에 등록해라.