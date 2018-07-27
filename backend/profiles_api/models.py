from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    #works with custom user manager
    def create_user(self, email, name, password=None):
    #creates a new user profile object
        if not email:
            raise ValueError('Users must have an email address')
    #to convert all email addresses to lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
    #this encrypts and hashes password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
    #creates the superuser with the above attributes        
        user =self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object =UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
    # gets user's full name
        return self.name

    def get_short_name(self):
    # used to get user's short name
        return self.name
    
    #Knows how to return a name as a string
    def __str__(self):
    #returning an object as a string
        return self.email
