from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password



class User(AbstractBaseUser, PermissionsMixin):
    id        = models.BigAutoField(primary_key=True)    
    username  = models.CharField('Username', max_length=25, unique=True)
    password  = models.CharField('Password', max_length=256)
    name      = models.CharField('Nombre', max_length=50)
    email     = models.EmailField('Email', max_length=60)

    def save(self, **kwargs):
        some_salt     = 'mJAFMjafai342akAA88KisJ8'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)