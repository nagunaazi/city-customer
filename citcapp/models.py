from django.db import models

class CityModel(models.Model):
    pin_code = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name


class CustomerModel(models.Model):
    cus_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    cno = models.IntegerField()
    city_pin = models.ForeignKey(CityModel, on_delete=models.CASCADE)