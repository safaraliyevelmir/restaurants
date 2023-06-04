from django.db import models



class Restaurant(models.Model):


    fire_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.name
    
