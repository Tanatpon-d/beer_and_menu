from django.db import models


class Beer(models.Model):
    name = models.CharField(max_length=255)
    beer_type = models.CharField(max_length=255)
    description = models.TextField()
    image = models.TextField()
    # image = models.ImageField(upload_to='beer_images/')


