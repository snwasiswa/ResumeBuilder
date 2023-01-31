from abc import ABC

from django.contrib.auth.models import Group

from .models import Education
from rest_framework import serializers
from django import forms
from allauth.account import adapter
# from drf_braces.serializers.form_serializer import FormSerializer
from rest_framework import serializers

# from rest_auth.registration.serializers import RegisterSerializer
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.password_validation import validate_password


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ['url', 'school', 'degree', 'major', 'minor', 'gpa', 'year', ]
