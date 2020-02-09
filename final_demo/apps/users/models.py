from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
from shortuuidfield import ShortUUIDField


class UserManager(BaseUserManager):
    def _create_user(self, telephone,username, email, password, **kwargs):
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')


        user = self.model(telephone=telephone,username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username, email,password,**kwargs):

        kwargs['is_superuser']=False
        return self._create_user(telephone=telephone,username=username, email=email,password= password, **kwargs)

    def create_superuser(self, telephone,username, email, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone,username=username,email= email, password=password, **kwargs)



class User(AbstractBaseUser,PermissionsMixin):
    """
    用户信息
    """
    uid = ShortUUIDField(primary_key=True)
    telephone=models.CharField(max_length=11,unique=True)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    # is_active = models.BooleanField(default=False)
    img = models.ImageField(upload_to='upload',default='default.jpg')#tumbnail文件上传！！！！！！


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username


