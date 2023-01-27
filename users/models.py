from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField
from localflavor.us.models import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES

from resume import settings


# Create your models here.

class User(AbstractUser):
    """Model for User"""
    address = models.CharField("Address line 1", max_length=1024)
    # zip_code = models.CharField("ZIP / Postal code", max_length=12,)
    zip_code = USZipCodeField()
    city = models.CharField("City", max_length=1024,)
    state = USStateField(choices=STATE_CHOICES)
    country = CountryField()
    phone = PhoneNumberField()
    personal_url1 = models.CharField("Url line 1", max_length=1024, blank=True, null=True)
    personal_url2 = models.CharField("Url line 2", max_length=1024, blank=True, null=True)
    personal_url3 = models.CharField("Url line 3", max_length=1024, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

    @property
    def get_avatar_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216377/media/avatars/defaultprofile_vad1ub.png"