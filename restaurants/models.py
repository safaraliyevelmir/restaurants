from django.db import models


class Interior(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PaymentOption(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ServiceOption(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DiningOption(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Amnetie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DietaryOption(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Restaurant(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    profile_img = models.ImageField(upload_to="restaurants/",null=True)
    reviews_count = models.IntegerField(default=0)
    visit_count = models.IntegerField(default=0)
    service_status = models.CharField(max_length=255,null=True)

    payment_option = models.ForeignKey(PaymentOption,on_delete=models.SET_NULL,related_name='restaurant_payment',null=True)
    service_option = models.ForeignKey(ServiceOption,on_delete=models.SET_NULL,related_name='restaurant_service',null=True)
    dining_option = models.ForeignKey(DiningOption,on_delete=models.SET_NULL,related_name='restaurant_diening',null=True)
    amenitie = models.ForeignKey(Amnetie,on_delete=models.SET_NULL,related_name='restaurant_amnetie',null=True)
    cuisine = models.ForeignKey(Cuisine,on_delete=models.SET_NULL,related_name='restaurant_cuisine',null=True)
    dietary_option = models.ForeignKey(DietaryOption,on_delete=models.SET_NULL,related_name='restaurant_dietary',null=True)
    interior = models.ForeignKey(Interior,on_delete=models.SET_NULL,related_name='restaurant_interior',null=True)

    fire_id = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.name
    
