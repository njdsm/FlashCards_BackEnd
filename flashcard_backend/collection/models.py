from django.db import models

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)


class Flashcard(models.Model):
    collection_id = models.ForeignKey(
        Collection, on_delete=models.CASCADE
    )
    front_text = models.CharField(max_length=250, null=True, blank=True)
    back_text = models.CharField(max_length=250, null=True, blank=True)

