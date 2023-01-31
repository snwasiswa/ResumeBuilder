from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'address', 'city', 'state', 'zip_code', 'country',
                  'phone', 'personal_url1', 'personal_url2', 'personal_url3', ]
