from django.urls import path, include
from chooseClass.api import views

urlpatterns = [
    path('getClasses/', views.GetClasses.as_view()),
    path('getClasses', views.GetClasses.as_view()),
    path('getPreCourses/<int:pk>', views.GetPreCourse.as_view()),
    path('getPreCourses/<int:pk>/', views.GetPreCourse.as_view()),
    path('getPeriCourses/<int:pk>', views.GetPeriCourse.as_view()),
    path('getPeriCourses/<int:pk>/', views.GetPeriCourse.as_view()),
    path('register', views.Register.as_view()),
    path('register/', views.Register.as_view()),
]
