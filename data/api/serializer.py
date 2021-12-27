from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import registration
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = registration
        fields = '__all__'