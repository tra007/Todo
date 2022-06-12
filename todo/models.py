from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class DateTimeManager(models.Manager):
    def get_queryset_user(self, user):
        return super().get_queryset().filter(owner=user)


# Create your models here.
class DateTime(models.Model):
    time = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    manage = DateTimeManager()
    objects=models.Manager()

    def __str__(self):
        return f"{self.owner} - {self.time}"


class ListToDo(models.Model):
    date = models.ForeignKey(DateTime, on_delete=models.CASCADE)
    job = models.CharField(max_length=150)
    start = models.TimeField(blank=True,null=True)
    finish = models.TimeField(blank=True,null=True)
    don = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)
