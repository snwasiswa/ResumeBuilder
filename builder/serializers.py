from .models import Education
from rest_framework import serializers


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ['url', 'school', 'degree', 'major', 'minor', 'gpa', 'year', ]
