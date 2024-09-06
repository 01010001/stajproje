from django.db import models
from datetime import date

class Teams(models.Model):
    team_active = models.BooleanField(default=True)
    team_name = models.CharField(max_length=99)


class Projects(models.Model):
    project_active = models.BooleanField(default=True)
    project_name = models.CharField(max_length=99)
    start_date = models.DateField(default=date.today, editable=True)
    end_date = models.DateField(default='', editable=True, blank=True, null=True)



#history kullanmak yerine gelistirici table guncellendigide yeni bir entry olusturulacak 
#bir tablonun aktif oldugu surec iki tane date field ile ifade edilecek. "insert-only databases"
class Developers(models.Model):
    developer_active = models.BooleanField(default=True)
    full_name = models.CharField(max_length=99)
    start_date = models.DateField(default=date.today, editable=True, null=True)
    end_date = models.DateField(default='', editable=True, blank=True, null=True)

    # Status = models.CharField(max_length=20, choices={"CURRENT": "current", })
    row_status = models.CharField(max_length=20, default="Current", null=True, blank=True)
    team = models.ManyToManyField(Teams, blank=True)
    project = models.ManyToManyField(Projects, through="WorkingOn", blank=True, related_name="Developers")

#one developer can be part of a variable amount of projects, date data needs to be stored for each project.
#intermediary table for the many-to-many relationships between Developers and Projects
class WorkingOn(models.Model):
    is_relation_active = models.BooleanField(default=False)
    developer = models.ForeignKey(Developers, on_delete=models.DO_NOTHING, related_name="works")
    project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING, related_name="works")
    start_date = models.DateField(default=date.today, editable=True)
    end_date = models.DateField(default='', editable=True, blank=True, null=True)
    status = models.CharField(max_length=50, default="working", null=True, blank=True)
    #status here?


