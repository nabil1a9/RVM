from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  Boutaille(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE, related_name = "boutaille",null = True)

    type = models.CharField(max_length=20,null=True)
    etat = models.CharField(max_length=20,null=True)
    cap = models.CharField(max_length=8,null = True)
    marque = models.CharField(max_length=25, null = True)
    def __str__(self):
        return self.type
RATE_CHOICES = [
(1, '1 trash'),
(2, '2 bad'),
(3, '3 ok'),
(4, '4 - good'),
(5,'5 perfect'),

]
class  Note(models.Model):
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return self.rate