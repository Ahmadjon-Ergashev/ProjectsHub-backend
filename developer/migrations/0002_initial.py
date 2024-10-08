# Generated by Django 5.1 on 2024-08-18 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('developer', '0001_initial'),
        ('project', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='projects',
            field=models.ManyToManyField(related_name='developers', to='project.project'),
        ),
        migrations.AddField(
            model_name='developer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='developer',
            name='skills',
            field=models.ManyToManyField(related_name='developers', to='developer.skill'),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='teams', to='developer.developer'),
        ),
        migrations.AddField(
            model_name='team',
            name='projects',
            field=models.ManyToManyField(related_name='teams', to='project.project'),
        ),
        migrations.AddField(
            model_name='team',
            name='team_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developer.developer'),
        ),
    ]
