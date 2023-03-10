from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length= 100, unique= True)
    
    def __str__(self):
        return self.locationName

#class MYSITEBASE2(models.Model): 
    #Title = models.CharField(max_length=100, blank=False)
    #Description = models.TextField(blank=True)
    #Date = models.DateField(blank=False)
    #Completed = models.BooleanField(default=False)
    
    #def __str__(self):
        #return self.Title
    
class Item(models.Model): 
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete= models.CASCADE)
   
    def __str__(self):
        return self.itemName