from django.db import models
from django.contrib.auth.models import User


class PlantStatus(models.Model):
    class Status(models.TextChoices):
        DEFAULT = 'Normal'
        GROWING = 'Growing'
        DEAD = 'Dead'
        HEALTHY = 'Healthy'
        FRUIT = 'Fruit'
        SICK = 'Sick'
        FLOWERS = 'Flowers'
        WATERING = 'Watering'
        PLANTING = 'Planting'
        WINTER = 'Winter'
        WILT = 'Wilt'

    plant = models.ForeignKey('plant.Plant', on_delete=models.CASCADE, null=False, related_name='statuses')
    info = models.TextField()
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DEFAULT)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    """
    attributes from foreign keys backward relation:
    * reactions (PlantStatusReaction)
    * comments (PlantStatusComment)
    """

    objects = models.Manager()

    @property
    def visible_comments(self):
        return getattr(self, 'comments').filter(visibility=True)

    class Meta:
        ordering = ['-published']
        verbose_name_plural = 'statuses' # not statuss
        indexes = [
            models.Index(fields=['published'])
        ]

    def __str__(self):
        return f"{self.plant} status: {self.status}"


class PlantStatusReaction(models.Model):
    class Reaction(models.TextChoices):
        GOOD = 'Good'
        SORRY = 'Sorry'
        HAHA = 'Haha'
        HATE = 'Hate'

    plant_status = models.ForeignKey(PlantStatus, on_delete=models.CASCADE, null=False, related_name='reactions')
    reaction = models.CharField(max_length=12, default=Reaction.GOOD, choices=Reaction.choices)
    authors_profile = models.ForeignKey('userprofile.UserProfile', null=True, on_delete=models.CASCADE, related_name='reactions_given') # all reactions
    uploaded = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"Reaction {self.reaction} of {self.authors_profile.user.username} to status {self.plant_status}"

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    def save(self, *args, **kwargs):
        reactions_to_status = self.plant_status.reactions
        if reactions_to_status.filter(authors_profile=self.authors_profile).exists():
            raise ValueError("You cannot make reaction multiple times.")
        if self.plant_status.plant.owners_profile == self.authors_profile:
            raise ValueError("User cannot make reaction to his own status.")
        return super().save(*args, **kwargs)


class PlantStatusComment(models.Model):
    class VisibleManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(visibility=True)

    plant_status = models.ForeignKey(PlantStatus, on_delete=models.CASCADE, null=False, related_name='comments')
    authors_profile = models.ForeignKey('userprofile.UserProfile', null=True, on_delete=models.CASCADE, related_name='comments_given')
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    visibility = models.BooleanField(default=True)

    objects = models.Manager()
    visible = VisibleManager()

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['published'])
        ]

    def __str__(self):
        return f"Comment to {self.plant_status} by {self.authors_profile.user.username}"


