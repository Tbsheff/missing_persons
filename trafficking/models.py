from django.db import models
from datetime import datetime, timedelta


class Missingperson(models.Model):
    date_missing = models.DateField(default=datetime.today, blank=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age_at_missing = models.CharField(max_length=3)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)

    def __str__(self):
        return (self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

# Create your models here.
