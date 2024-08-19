from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="projects/logos/")
    banner = models.ImageField(upload_to="projects/banners/")
    website = models.URLField(blank=True, null=True)
    repo_url = models.URLField(blank=True, null=True)
    elevator_pitch = models.FileField(upload_to="projects/elevator_pitch/")
    tags = models.ManyToManyField(Tag, related_name="projects")
    developer = models.ForeignKey("developer.Developer", on_delete=models.SET_NULL, related_name="developer_projects", blank=True, null=True)
    team = models.ForeignKey("developer.Team", on_delete=models.SET_NULL, related_name="team_projects", blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name