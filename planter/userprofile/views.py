from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def profiles_list_view(request, *args, **kwargs):
    statistics = {
        'max': {
            'plants': UserProfile.objects.get_most_plants_userprofile(),
            'statuses': None,
            'comments_given': None,
            'comments_obtained': None,
            'reactions_given': None,
            'reactions_obtained': None,
        },
        'avg': {
            'plants': None,
        }
    }
    return render(request,
                  'userprofile/userprofile/list.html',
                  context={
                      'userprofiles' : UserProfile.objects.all(),
                      'statistics' : statistics,
                  })

def profile_detail_view(request, *args, slug=None, **kwargs):
    print('...', args, slug, kwargs)
    u_profile = get_object_or_404(UserProfile, slug=slug)
    return render(request,
                  'userprofile/userprofile/detail.html',
                  context={
                      'userprofile': u_profile,
                      'plants': u_profile.plants.all(),
                  })
