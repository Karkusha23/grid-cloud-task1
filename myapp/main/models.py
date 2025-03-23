from django.db import models

class MyModel(models.Model):
    textfield = models.TextField()
    intfield = models.IntegerField(default=0)
    boolfield = models.BooleanField(default=False)

# Create your models here.
