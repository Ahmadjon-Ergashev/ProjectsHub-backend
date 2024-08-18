from django.db import models

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    avatar = models.ImageField(upload_to="customers/avatars/")
    banner = models.ImageField(upload_to="customers/avatars/banner/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"