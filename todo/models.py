from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    body = models.CharField(max_length=200)