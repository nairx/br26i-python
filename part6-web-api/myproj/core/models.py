from django.db import models

from django.db import models

class todo(models.Model):
    task=models.CharField(max_length=50)


class product(models.Model):
    name=models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=20)

