from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones
from plant.models import Plant, PlantType
from plantstatus.models import PlantStatus, PlantStatusReaction, PlantStatusComment
from django.utils.text import slugify
from django.db.models import Count, F


class UserProfile(models.Model):
    class UserProfileManager(models.Manager):
        def get_by_username(self, username):
            return self.get(user__username=username)

        def get_most_plants_userprofile(self):
            return self.annotate(Count('plants')).order_by('-plants__count').first()


    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userprofile')
    photo = models.ImageField(blank=True, upload_to="user/%Y/%m/%d/")
    slug = models.SlugField(max_length=200)

    TZ_CHOICES = tuple(available_timezones())
    TZ_MAX_LEN = max(map(lambda s: len(s), TZ_CHOICES))
    timezone = models.CharField(max_length=TZ_MAX_LEN, choices=tuple(zip(TZ_CHOICES, TZ_CHOICES)), default='UTC')

    objects = UserProfileManager()

    def get_local_datetime(self):
        return datetime.now(tz=ZoneInfo(str(self.timezone)))

    def get_local_date(self):
        return self.get_local_datetime().date()

    def get_local_time(self):
        return self.get_local_datetime().time()

    def __str__(self):
        return f"Profile of {self.user.username}"

    def get_absolute_url(self):
        return reverse('userprofile:userprofile_detail', args=[self.slug])

    """
    attributes from foreign keys backward relation:
    * plants (Plant)
    * reactions_given (PlantStatusReaction)
    * comments_given (PlantStatusComment)
    * 
    """

    @property
    def statuses_of_plants(self):
        plants_ids = self.plants.values_list('id', flat=True)
        return PlantStatus.objects.filter(plant__id__in=plants_ids)

    @property
    def reactions_obtained(self):
        statuses = self.statuses_of_plants
        return PlantStatusReaction.objects.filter(plant_status__in=statuses)

    @property
    def comments_obtained(self):
        statuses = self.statuses_of_plants
        return PlantStatusComment.objects.filter(plant_status__in=statuses)