from django.db import models

class Pop(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=20)
    pas = models.IntegerField()


def __str__(self):
    return self.name