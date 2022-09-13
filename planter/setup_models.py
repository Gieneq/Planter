import os

from django.contrib.auth.models import User
from plant.models import Plant, PlantType
from userprofile.models import UserProfile
from plantstatus.models import PlantStatus, PlantStatusComment, PlantStatusReaction
from django.utils.text import slugify

def reset_db():
    cmds = []
    cmds.append(r'pwd')
    cmds.append(r'find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
    cmds.append(r'find . -path "*/migrations/*.pyc"  -delete')
    cmds.append(r'find . -path "*/db.sqlite3" -delete')
    cmds.append(r'python manage.py makemigrations')
    cmds.append(r'python manage.py migrate')

    for cmd in cmds:
        os.system(cmd)
reset_db()

def setup_superuser():
    print('SUPERUSER')
    user_pyrograf = User.objects.filter(username='pyrograf')
    if user_pyrograf.exists():
        user_pyrograf.delete()
    user_pyrograf = User.objects.create_user('pyrograf', 'pyrograf.pl@gmail.com', 'wentka12', is_superuser=True, is_staff=True)
    # user_pyrograf.save()
    print(user_pyrograf.check_password('wentka12'))
    print(f"{user_pyrograf.is_superuser=}")
    print(f"{user_pyrograf.is_staff=}")
setup_superuser()


def setup_users():
    print('USERS')
    def regenerate_user(id):
        username = f'user_{id}'
        user = User.objects.filter(username=username)
        if user.exists():
            user.delete()
        user = User.objects.create_user(username, f'test.{id}.user@gmail.com', 'test')
        # user.save()
    for i in range(30):
        regenerate_user(i)
setup_users()


def setup_planttypes():
    print('PLANT TYPES')
    def regenerate_planttype(id):
        name = f'planttype_{id}'
        slug = slugify(name)
        planttype = PlantType.objects.filter(name=name)
        if planttype:
            planttype.delete()
        planttype = PlantType.objects.create(name=name, slug=slug, origin='IDK')
        # planttype.save()
    for i in range(12):
        regenerate_planttype(i)
setup_planttypes()


def setup_plant():
    print('PLANTS')
    def regenerate_plant(id):
        name = f'plant_{id}'
        slug = slugify(name)
        type = PlantType.objects.all().order_by('?').first()
        owners_profile = UserProfile.objects.all().order_by('?').first()
        plant = Plant.objects.filter(name=name)
        if plant:
            plant.delete()
        plant = Plant.objects.create(name=name, slug=slug, type=type, owners_profile=owners_profile)
        plant.save()
    for i in range(70):
        regenerate_plant(i)
setup_plant()

def setup_plantstatus():
    print('STATUSES')
    statuses = PlantStatus.objects.all()
    statuses.delete()
    def regenerate_plantstatus(id):
        plant = Plant.objects.order_by('?').first()
        info = 'Something more or less interesting.'
        STATUSES_LUT = [PlantStatus.Status.GROWING, PlantStatus.Status.DEFAULT, PlantStatus.Status.HEALTHY, PlantStatus.Status.WATERING]
        status = STATUSES_LUT[id % 4]
        instance = PlantStatus.objects.create(plant=plant, info=info, status=status)
        # instance.save()
    for i in range(150):
        regenerate_plantstatus(i)
setup_plantstatus()

def setup_plantcomments():
    print('COMMENTS')
    instances = PlantStatusComment.objects.all()
    instances.delete()
    def regenerate_plantcomments(id):
        plant_status = PlantStatus.objects.order_by('?').first()
        authors_profile = UserProfile.objects.order_by('?').first()
        content = 'blah blah'
        instance = PlantStatusComment.objects.create(plant_status=plant_status, content=content, authors_profile=authors_profile)
        # instance.save()
    for i in range(100):
        regenerate_plantcomments(i)
setup_plantcomments()

def setup_plantreaction():
    print('REACTIONS')
    instances = PlantStatusReaction.objects.all()
    instances.delete()
    def regenerate_plantr(id):
        plant_status = PlantStatus.objects.order_by('?').first()
        owner = plant_status.plant.owners_profile.user
        used_authors = plant_status.reactions.values_list('authors_profile__id', flat=True)
        available_author = User.objects.exclude(id__in=used_authors).exclude(id=owner.id).order_by('?').first()
        REACTIONS_LUT = [PlantStatusReaction.Reaction.GOOD, PlantStatusReaction.Reaction.HAHA, PlantStatusReaction.Reaction.HATE]
        reaction = REACTIONS_LUT[id%3]
        # print('@', id, plant_status, author, reaction)
        try:
            instance = PlantStatusReaction.objects.create(plant_status=plant_status, reaction=reaction, authors_profile=available_author.userprofile)
        except ValueError as e:
            print('Attempt to make bad comment', e)
        # instance.save()
    for i in range(200):
        regenerate_plantr(i)
    print('Comments count:', len(PlantStatusReaction.objects.all()))
setup_plantreaction()


os.system(r'python manage.py runserver')


# user = User.objects.get(username='user_4')
# print(userprofile := user.userprofile)
# up = UserProfile.objects.get_by_username('pyrograf')
# print(up.plants.count(), 'Owned plants: ', (plants_ids := userprofile.plants.values_list('id', flat=True)).count())
# print(up.get_statuses_of_plants().count(), 'Statuses of owned plants: ', (statuses := PlantStatus.objects.filter(plant__id__in=plants_ids)).count())
# print('Reactions given: ', user.reactions_given.count())
# print(up.get_reactions_obtained().count(), 'Reactions obtained: ', (reactions_obtained := PlantStatusReaction.objects.filter(plant_status__in=statuses)).count())
# # print(*reactions_obtained.all(), sep='\n')
# print('Comments given: ', user.comments_given.count())
# print(up.get_comments_obtained().count(), 'Comments obtained: ', (comments_obtained := Comment.objects.filter(plant_status__in=statuses)).count())
# # print(*comments_obtained.all(), sep='\n')
# todo przenieść to do profilu usera