from django.db import models
from django.urls import reverse
from plantstatus.models import PlantStatusComment, PlantStatusReaction
from django.contrib.auth.models import User
from django.utils.text import slugify


class PlantType(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, default='Nothing written here.')
    preferences = models.TextField(null=True, default='Nothing written here.')
    origin = models.CharField(max_length=200, default='', null=True)
    photo = models.ImageField(blank=True, upload_to="planttype/")

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant:planttype_detail', args=[self.slug])


class Plant(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    type = models.ForeignKey(PlantType, null=True, related_name='examples', on_delete=models.SET_NULL)
    owners_profile = models.ForeignKey('userprofile.UserProfile', null=False, on_delete=models.CASCADE, related_name='plants')

    objects = models.Manager()

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


    """
    attributes from foreign keys backward relation:
    * statuses (PlantStatus)
    * sensor (Sensor)
    """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant:plant_detail', args=[self.owners_profile.user.username, self.slug])

    @property
    def last_status(self):
        return self.statuses.order_by('-published').first()

    @property
    def all_comments(self):
        return PlantStatusComment.objects.filter(plant_status__in=self.statuses.all())

    @property
    def all_reactions(self):
        return PlantStatusReaction.objects.filter(plant_status__in=self.statuses.all())







    # def get_default_action_status():
    #     """ get a default value for action status; create new status if not available """
    #     return ActionStatus.objects.get_or_create(name="created")[0]
    #
    #     def get_default_action_result():
    #         """ get a default value for result status; create new result if not available """
    #
    #     return ActionResult.objects.get_or_create(name="unknown")[0]
    #
    #     class ActionStatus(models.Model):
    #         """ table to track statuses of actions, such as 'created', 'started', 'completed', etc. """
    #
    #     name = models.CharField(max_length=16, unique=True)
    #
    #     class ActionResult(models.Model):
    #         """ table to track results of actions, such as 'passed', 'failed', 'unknown', etc. """
    #
    #     name = models.CharField(max_length=16, unique=True)
    #
    #     class Action(models.Model):
    #         """ table to track individual actions """
    #
    #     name = models.CharField(max_length=16, unique=True)
    #     status = models.ForeignKey(ActionStatus, default=get_default_action_status, on_delete=models.CASCADE)
    #     result = models.ForeignKey(ActionResult, default=get_default_action_result, on_delete=models.CASCADE)
