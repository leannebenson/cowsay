from django.db import models

# Create your models here.

class Cowsay(models.Model):
    input = models.TextField(max_length=80)

    def __str__(self):
        return self.input