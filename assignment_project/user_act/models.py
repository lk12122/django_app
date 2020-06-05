from django.db import models

# Create your models here.


from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_tz = models.CharField(max_length=200)


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
