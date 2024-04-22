from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


class Token(models.Model):
    rand_token = models.UUIDField()
