from django.urls import path, include
from comment.api import views

urlpatterns = [
    path('getComments/', views.GetComment.as_view()),
    path('getComments', views.GetComment.as_view()),
    path('setComments/', views.SetComment.as_view()),
    path('setComments', views.SetComment.as_view()),
]
