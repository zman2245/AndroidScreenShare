from django.db import models

class Click(models.Model):
    xpercent = models.FloatField()
    ypercent = models.FloatField()
    is_valid = models.BooleanField()

class Screen(models.Model):
    email = models.CharField(max_length=200)
    pid_screen_process = models.IntegerField()
    web_sever_port = models.IntegerField()
