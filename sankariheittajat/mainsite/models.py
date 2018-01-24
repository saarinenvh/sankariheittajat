from django.db import models
from django.utils import timezone



class uutiset(models.Model):
    aihe = models.CharField(max_length=255);
    uutinen = models.TextField();
    kirjoittaja = models.CharField(max_length=255);
    aika = models.DateTimeField(timezone.now());

    def __str__(self):
        return '%s' % (self.aihe)

    class Meta:
        ordering = ['aika']

# Create your models here.
