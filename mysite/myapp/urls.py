from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'myapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('article1/', views.article1, name='article1'),
    path('article2/', views.article2, name='article2'),
    path('post/', views.post, name='post'),
    path('social/', views.social, name='social'),
    path('base/', views.post, name='base'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('eduinfo/', views.edu_info, name='edu_info'),
    path('event/', views.event, name='event'),
]
