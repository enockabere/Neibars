from django.urls import path
from  . import views

urlpatterns = [
    path('pro', views.create_account,name="create_pro"),
    path('dashboard', views.dashboard,name="dash"),
    path('personal', views.personal,name="personal"),
    path('business', views.business,name="business"),
    path('search', views.b_search,name="search"),
    path('amenities', views.amenities,name="amenities"),
    path('sidebar', views.sidebar,name="sidebar"),
    path('addbiz', views.create_biz,name="addbiz"),
    path('addamenity', views.create_amenity,name="addamenity"),
    path('like/',views.like_post,name="like_post" ),
]
