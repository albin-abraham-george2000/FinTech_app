from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class User(AbstractUser):
    """Custom user model"""
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True, verbose_name='groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True, verbose_name='user permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission


# class User(AbstractUser):
#     """Custom user model"""
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def _str_(self):
#         return self.username

# # Define ManyToMany relationships with unique related_name arguments
# Group.add_to_class('users', models.ManyToManyField(User, verbose_name=('users'), blank=True, related_name='custom_groups'))
# Permission.add_to_class('users', models.ManyToManyField(User, verbose_name=('users'), blank=True, related_name='custom_user_permissions'))
