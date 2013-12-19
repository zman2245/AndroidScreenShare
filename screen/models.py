from django.db import models

class Click(models.Model):
    xpercent = models.FloatField()
    ypercent = models.FloatField()
    is_valid = models.BooleanField()
