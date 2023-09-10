
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    is_children = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    name = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    parent = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name
