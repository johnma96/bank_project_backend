from django.db import models
from .user     import User
from backend.authAppExample.models import user

class Account(models.Model):
    id             = models.AutoField(primary_key=True)
    user           = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance        = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive       = models.BooleanField(default=True)

    
