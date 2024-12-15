from django.db import models

# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name
    

class Game(models.Model):
    title = models.CharField(max_length= 100)
    developer = models.ForeignKey(Developer , on_delete=models.PROTECT)
    