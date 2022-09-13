from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Plant, PlantType
from userprofile.models import UserProfile


class PlantTypeList(ListView):
    # queryset = PlantType.objects.all()
    def get_queryset(self):
        if 'slug' not in self.kwargs:
            return PlantType.objects.all()
        return PlantType.objects.filter(slug=self.kwargs['slug'])

    context_object_name = 'planttypes'
    template_name = 'plant/planttype/list.html'


def plant_list_view(request, planttype_slug=None):
    if planttype_slug is not None:
        plants = Plant.objects.filter(type__slug=planttype_slug)
    else:
        plants = Plant.objects.all()
    planttype = PlantType.objects.filter(slug=planttype_slug).first()
    return render(request=request,
                  template_name='plant/plant/list.html',
                  context={
                      'plants': plants,
                    'planttype': planttype})


def plant_detail_view(request, username=None, slug=None):
    userprofile = UserProfile.objects.get_by_username(username)
    plant = get_object_or_404(Plant, owners_profile=userprofile, slug=slug)
    return render(request=request,
                  template_name='plant/plant/detail.html',
                  context={'plant': plant})

