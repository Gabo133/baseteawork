# # -*- coding: utf-8 -*-
# from django.db import models
# from retro_auth.defines import *
# from django.contrib.auth.models import User

# # Create your models here.
# class UserProfile(models.Model):
#     user = models.ForeignKey(User,null=True,default=None,on_delete=models.CASCADE)
#     rut = models.CharField(max_length=12, default="Sin Rut")
    
#     def __str__(self):
#         return "%s %s Rut: %s" % (self.user.first_name, self.user.last_name, self.rut)