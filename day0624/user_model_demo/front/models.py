from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.

#User.objects.all()
#Person.objecys.all()等价的，person只是代理，全部使用user的
# class Person(User):
#     class Meta:
#         proxy=True
#     @classmethod#表示这是一个类方法
#     def get_black_list(self):
#         return  self.objects.filter(is_active=False)

# class UserExtension(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
#     telephone=models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3578]\d{9}')])
#     school=models.CharField(max_length=30)
#     #当user模型有新用户，需发送信号，通知扩展，receiver接收
#
#     @receiver(post_save,sender=User)
#     def handler_user_extension(sender,instance,created,**kwargs):
#         if created:#创建
#             UserExtension.objects.create(user=instance)
#         else:#更新
#             instance.extension.save()

class UserManager(BaseUserManager):
    use_in_migrations = True
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

    def create_superuser(self, username, email, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(username=username,email= email, password=password, **kwargs)


# class User(AbstractUser):
#     telephone = models.CharField(max_length=11, validators=[validators.RegexValidator(r'1[3578]\d{9}')],unique=True)
#     school=models.CharField(max_length=30)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'telephone'#3默认采用username验证，我们修改为telephone

class User(AbstractBaseUser,PermissionsMixin):
    telephone=models.CharField(max_length=11,unique=True)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='articles')
    class Meta:
        permissions=[
            ('view_article','看文章的权限')
        ]

