# Generated by Django 5.1 on 2024-08-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectschedule', '0003_alter_developers_end_date_alter_developers_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developers',
            name='end_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='workingon',
            name='end_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
