# Generated by Django 5.1 on 2024-08-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
