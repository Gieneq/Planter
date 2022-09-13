# Generated by Django 4.1.1 on 2022-09-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('status', models.CharField(choices=[('Normal', 'Default'), ('Growing', 'Growing'), ('Dead', 'Dead'), ('Healthy', 'Healthy'), ('Fruit', 'Fruit'), ('Sick', 'Sick'), ('Flowers', 'Flowers'), ('Watering', 'Watering'), ('Planting', 'Planting'), ('Winter', 'Winter'), ('Wilt', 'Wilt')], default='Normal', max_length=12)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='plant.plant')),
            ],
            options={
                'verbose_name_plural': 'statuses',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='PlantStatusReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(choices=[('Good', 'Good'), ('Sorry', 'Sorry'), ('Haha', 'Haha'), ('Hate', 'Hate')], default='Good', max_length=12)),
                ('uploaded', models.DateTimeField(auto_now=True)),
                ('authors_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions_given', to='userprofile.userprofile')),
                ('plant_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='plantstatus.plantstatus')),
            ],
        ),
        migrations.CreateModel(
            name='PlantStatusComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('visibility', models.BooleanField(default=True)),
                ('authors_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_given', to='userprofile.userprofile')),
                ('plant_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='plantstatus.plantstatus')),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
        migrations.AddIndex(
            model_name='plantstatuscomment',
            index=models.Index(fields=['published'], name='plantstatus_publish_22ed09_idx'),
        ),
        migrations.AddIndex(
            model_name='plantstatus',
            index=models.Index(fields=['published'], name='plantstatus_publish_f2a533_idx'),
        ),
    ]
