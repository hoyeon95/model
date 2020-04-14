from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title   # Tip : Blog object(1) 이라는 제목을 내가 실제로 단 title로 바꿔줌