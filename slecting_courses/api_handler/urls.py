from django.urls import path, include

urlpatterns = [
    path('enter/', include('login.api.urls')),
    path('university/', include('chooseClass.api.urls')),
    path('comment/', include('comment.api.urls')),
    path('myPlan/', include('myPlan.api.urls')),
]

