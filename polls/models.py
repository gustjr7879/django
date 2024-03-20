from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):#models -> 장고의 모델임을 명시함. 이 코드로 Post가 데이터베이스에 저장해야 된다는 것을 알게됨
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) #다른 모델에 대한 링크
    title = models.CharField(max_length = 200)# 글자수가 제한된 텍스트를 정의할 때 사용, 짧은 문자열
    text = models.TextField()#글자수 제한이 없는 긴 텍스트를 위함
    create_date = models.DateTimeField(#날짜와 시간
        default = timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title #__str__로 title을 얻을 수 있게함