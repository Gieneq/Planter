from django.urls import path
from .views import plant_list_view, plant_detail_view, PlantTypeList

app_name = 'plant'

urlpatterns = [
    path('', plant_list_view, name='plant_list'),

    path('atlas/', PlantTypeList.as_view(), name='planttype_list'),
    path('atlas/<slug:slug>/', PlantTypeList.as_view(), name='planttype_detail'),

    path('<slug:planttype_slug>/', plant_list_view, name='plant_list_by_type'),
    path('<slug:username>/<slug:slug>', plant_detail_view, name='plant_detail'),
]