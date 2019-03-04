from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('',  views.IndexView.as_view(), name='index'),
    # ex: /polls/   CBV의 generic view를 이용하여 url을 처리

    path('photos/', views.photos, name='photos'),
    path('upload/', views.upload, name='upload'),

    # ex: /polls/timeline/
]
