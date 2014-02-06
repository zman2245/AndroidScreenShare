from django.db import models

class Screen(models.Model):
    email = models.CharField(max_length=200)
    app_name = models.CharField(max_length=300)
    pid_screen_process = models.IntegerField()
    web_sever_port = models.IntegerField()
