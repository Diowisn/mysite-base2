from django.shortcuts import render
from PIL import Image
from rest_framework import generics
from .serializers import ItemSerializer, LocationSerializer
from .models import Item, Location


# Create your views here.

def index(request): 
    return render(request, 'posting/index.html')

def about(request):
    return render(request, 'posting/about.html')

def contact(request):
    return render(request, 'posting/contact.html')

def kebijkanprivasi(request):
    return render(request, 'posting/kebijakanprivasi.html')


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation= location)
        return queryset
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
    
class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    
    
    

#class ListMYSITEBASE2(generics.ListAPIView):
    #queryset = MYSITEBASE2.objects.all()
    #serializer_class = MYSITEBASE2Serializer
    
#class DetailMYSITEBASE2(generics.RetrieveUpdateAPIView):
    #queryset = MYSITEBASE2.objects.all()
    #serializer_class = MYSITEBASE2Serializer
    
#class CreateMYSITEBASE2(generics.CreateAPIView):
    #queryset = MYSITEBASE2.objects.all()
    #serializers_calss = MYSITEBASE2Serializer
    
#class DeleteMYSITEBASE2(generics.DestroyAPIView):
    #queryset = MYSITEBASE2.objects.all()
    #serializer_class = MYSITEBASE2Serializer
    
    
