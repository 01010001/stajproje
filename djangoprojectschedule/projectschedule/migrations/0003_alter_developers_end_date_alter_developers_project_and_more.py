# Generated by Django 5.1 on 2024-08-14 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectschedule', '0002_alter_developers_project_alter_developers_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developers',
            name='end_date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='developers',
            name='project',
            field=models.ManyToManyField(blank=True, related_name='Developers', through='projectschedule.WorkingOn', to='projectschedule.projects'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='workingon',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='works', to='projectschedule.developers'),
        ),
        migrations.AlterField(
            model_name='workingon',
            name='end_date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='workingon',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='works', to='projectschedule.projects'),
        ),
    ]
