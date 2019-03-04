from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import PhotoForm
from .models import Photo
from .models import Test

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

class IndexView(TemplateView):
    template_name = 'polls/index.html'

@login_required
def photos(request):
    sort = request.GET.get('sort','') #url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    User = get_user_model()
    user = get_object_or_404(User, username=request.user.username)
    #
    if sort == 'tags':
        photos = user.photo_set.order_by('-tags', '-created')
    else:
        photos = user.photo_set.order_by('-created')
    #
    ctx = {
        'user': user,
        'photos': photos,
    }
    #
    image_url=[]
    image_tag=[]
    image_name=[]
    for p in photos:
        image_url.append(p.image.url)
        image_tag.append(p.tags)
        image_name.append(p.image.name)
    #
    return render(request, 'polls/photos.html',{'image_url': image_url,'image_tag': image_tag,'image_name': image_name})
    
import os
from shutil import copyfile
import subprocess

@login_required
def upload(request):
    if request.method == "POST":
        #Get the posted form
        MyPhotoForm = PhotoForm(request.POST, request.FILES)
        if MyPhotoForm.is_valid():
            test = Test()
            photo = Photo()

            test.image = MyPhotoForm.cleaned_data["image"]
            test.save()
            subprocess.call(['python','C:/Tmp/inference.py'])
            os.remove('C:/Users/shael/mysite/media/test/test.png')

            photo.owner = User.objects.get(username=request.user.username)
            photo.image = MyPhotoForm.cleaned_data["image"]

            f = open('C:/Users/shael/mysite/tags.txt', 'rb')
            lines = f.readlines()
            print(lines)
            photo.tags = lines

            photo.save()
            print('Upload Success!!!!')
    else:
        MyPhotoForm = PhotoForm()
    return render(request, 'polls/upload.html')
