from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import User

def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    #from random import choice
    #import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    #arr = [choice(string.ascii_letters) for _ in range(8)]
    #pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    #extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s' % (instance.owner.username, filename) # 예 : wayhome/abcdefgs.png

def test_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    #from random import choice
    #import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    #arr = [choice(string.ascii_letters) for _ in range(8)]
    #pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    #extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s' % ('C:/Users/shael/mysite/media/test/test.png') # 예 : wayhome/abcdefgs.png
class Test(models.Model):
    image = models.ImageField(null=True, upload_to = test_path)

class Photo(models.Model):
    owner = models.ForeignKey(User, default = 1, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to = user_path)
    created = models.DateTimeField(default=timezone.now, blank=True)
    tags = models.CharField(max_length=100, blank=True)
