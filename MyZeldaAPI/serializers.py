from django.db.models import fields
from rest_framework import serializers
from .models import Personnage
 
class PersonnageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnage
        fields = ['nom']