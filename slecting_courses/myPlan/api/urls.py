from django.urls import path
from myPlan.api import views

urlpatterns = [
    path('getPlans/', views.GetPlans.as_view()),
    path('getPlans', views.GetPlans.as_view()),
    path('createPlan/', views.CreatePlan.as_view()),
    path('createPlan', views.CreatePlan.as_view()),
    path('register', views.Register.as_view()),
    path('register/', views.Register.as_view()),
    path('uRegister/', views.UpdateRegister.as_view()),
    path('uRegister', views.UpdateRegister.as_view()),
]
