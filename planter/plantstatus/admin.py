from django.contrib import admin
from .models import PlantStatus, PlantStatusReaction, PlantStatusComment

admin.site.register(PlantStatus)
admin.site.register(PlantStatusReaction)
admin.site.register(PlantStatusComment)
