from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Item, Location

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #fields = ('Title', 'Description', 'Completed')
        fields = ('__all__')


#class GroupSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = Group
        #fields = ['url', 'name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')