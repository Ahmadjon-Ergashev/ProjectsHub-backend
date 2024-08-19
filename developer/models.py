from django.db import models
from user.models import User

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    github = models.URLField()
    avatar = models.ImageField(upload_to="developers/avatars/")
    banner = models.ImageField(upload_to="developers/avatars/banner/")
    cv = models.FileField(upload_to="developers/cv/")
    skills = models.ManyToManyField(Skill, related_name="developers")
    projects = models.ManyToManyField("project.Project", related_name="developers")
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    avatar = models.ImageField(upload_to="teams/avatars/")
    banner = models.ImageField(upload_to="teams/avatars/banner")
    team_leader = models.ForeignKey(Developer, on_delete=models.CASCADE)
    members = models.ManyToManyField(Developer, related_name="teams")
    projects = models.ManyToManyField("project.Project", related_name="teams")
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name