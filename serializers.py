from rest_framework import serializers
from api1.models import Company

class Companyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__" #so we can get all fields from class mainapi from model





