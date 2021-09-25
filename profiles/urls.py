from django.urls import path
from  . import views

urlpatterns = [
    path('pro', views.create_account,name="create_pro"),
    path('dashboard', views.dashboard,name="dash"),
]
