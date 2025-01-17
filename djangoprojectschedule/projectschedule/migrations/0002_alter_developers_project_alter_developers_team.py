# Generated by Django 5.1 on 2024-08-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectschedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developers',
            name='project',
            field=models.ManyToManyField(blank=True, through='projectschedule.WorkingOn', to='projectschedule.projects'),
        ),
        migrations.AlterField(
            model_name='developers',
            name='team',
            field=models.ManyToManyField(blank=True, to='projectschedule.teams'),
        ),
    ]
