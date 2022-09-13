# Generated by Django 4.1.1 on 2022-09-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(default='Nothing written here.', null=True)),
                ('preferences', models.TextField(default='Nothing written here.', null=True)),
                ('origin', models.CharField(default='', max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='planttype/')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('owners_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='userprofile.userprofile')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='examples', to='plant.planttype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='plant',
            index=models.Index(fields=['name'], name='plant_plant_name_0c655e_idx'),
        ),
    ]