from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register_request,name="register"),
    path('', views.login_request, name="login"),
    
]
