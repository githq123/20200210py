from django.db import models

# Create your models here.
class FrontUser(models.Model):
    username=models.CharField(max_length=100)
    def __str__(self):
        return "<FrontUser:(id:%s,username:%s)>"%(self.id,self.username)
class UserExtension(models.Model):
    school=models.CharField(max_length=100)
    user=models.OneToOneField("FrontUser",on_delete=models.CASCADE,related_name="extensions")

    def __str__(self):
        return "<UserExtension:(school:%s,user_id:%s)>"%(self.school,self.user_id)