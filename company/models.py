from django.db import models

# Create your models here.

class Company(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to="companies/logos/")
    banner = models.ImageField(upload_to="companies/banners/")
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
