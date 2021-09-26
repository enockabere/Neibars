from django.urls import path
from  . import views

urlpatterns = [
    path('pro', views.create_account,name="create_pro"),
    path('dashboard', views.dashboard,name="dash"),
    path('personal', views.personal,name="personal"),
    path('business', views.business,name="business"),
    path('search', views.b_search,name="search"),
    path('amenities', views.amenities,name="amenities"),
]
