from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import *
from soji_back import settings


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.TextField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'price': self.price
        }


class Review(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username.__str__(),
            'text': self.text,
            'date': self.date
        }
