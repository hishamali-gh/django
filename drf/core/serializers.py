# MODELSERIALIZER
from rest_framework import serializers

from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    is_adult = serializers.SerializerMethodField() # A custom computed field that doesn't exist in the database!

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'is_adult']  # Or use '__all__' if you want every field

    # Custom Computed Field Logic:
    def get_is_adult(self, obj):
        return obj.age >= 18

    # Field-Level Validation:
    def validate_age(self, val):
        if val < 1:
            raise serializers.ValidationError('Enter a valid age input')

        return val

    # Field-Level Validation:
    def validate_name(self, val):
        if any(c.isdigit() for c in val):
            raise serializers.ValidationError('Name cannot contain numbers')

        return val

# SERIALIZER (REGULAR)
""" from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data) """
