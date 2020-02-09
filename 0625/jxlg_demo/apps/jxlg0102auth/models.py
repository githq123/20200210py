from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField
from django.core import validators
# Create your models here.

class UserManager:
    use_in_migrations = True

    def _create_user(self,telephone, username,  password, **kwargs):
        """
        Create and save a user with the given username, email, and password.
        """
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError('The given password must be set')

        user = self.model(username=username, telephone=telephone,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,telephone,username, password, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(telephone,username, password, **kwargs)

    def create_superuser(self,telephone, username, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(telephone,username, password, **kwargs)



class User(AbstractBaseUser,PermissionsMixin):
    uid=ShortUUIDField(primary_key=True)
    telephone=models.CharField(max_length=11,unique=True,validators=[validators.RegexValidator()])
    email=models.EmailField(unique=True,null=True)
    username=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    data_joined=models.DateTimeField(auto_now_add=True)


    EMAIL_FIELD = 'TELTPHONE'
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['email']

    objects=UserManager()
    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username