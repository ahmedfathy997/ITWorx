from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.image} {self.description}"


class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.email} {self.password}"

