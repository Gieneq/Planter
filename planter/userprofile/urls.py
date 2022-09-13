from django.urls import path
from .views import profiles_list_view, profile_detail_view

app_name = 'userprofile'

urlpatterns = [
    path('', profiles_list_view, name='userprofile_list'),
    path('<slug:slug>/', profile_detail_view, name='userprofile_detail'),
]