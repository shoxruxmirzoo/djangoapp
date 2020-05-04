from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    id = models.IntegerField(unique = True)

    def __str__(self):
        return self.name
