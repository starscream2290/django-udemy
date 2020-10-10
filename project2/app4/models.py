from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    email = models.EmailField(max_length=128,unique=True)
