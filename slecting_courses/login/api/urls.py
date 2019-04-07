from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from login.api import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('signup/', views.Signup.as_view()),
    path('login', views.Login.as_view()),
    path('signup', views.Signup.as_view()),
    path('getInfo', views.GetInfo.as_view()),
    path('getInfo/', views.GetInfo.as_view()),
    path('upInfo', views.UpInfo.as_view()),
    path('upInfo/', views.UpInfo.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
