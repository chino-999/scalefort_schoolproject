from rest_framework import serializers
from .models import School, Student


class SchoolSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = School

        fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student

        fields = '__all__'
