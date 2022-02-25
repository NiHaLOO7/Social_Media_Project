from django.db import models
from django.contrib import auth

# Create your models here.
#Django automatically creates a user model for us
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

