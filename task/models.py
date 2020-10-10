from django.db import models
from django.contrib.auth import models as Usermodel # pylint: disable=W0611
from datetime import datetime
from django.utils.timezone import now
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(Usermodel.User, on_delete=models.CASCADE, null= True)
    title = models.CharField(max_length=1000)
    is_done =  models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    finished_date = models.DateTimeField(null=True)


    def __str__(self):
        return self.title
