from django.db import models

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)


