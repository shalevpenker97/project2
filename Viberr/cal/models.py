from django.contrib.auth.models import Permission, User
from django.db import models


class My_Calender(models.Model):
    website_name      = models.CharField(max_length=250)
    website_placement = models.CharField(max_length=250)
    calender_image    = models.CharField(max_length=250,default='open')

    def get_calender_spots(self):
        return Calender_spot.objects.filter(My_Calender=self)

    def get_calender_spots_id(self):#This will return an array representation of objects
        spot_id_array =[]
        for spot in self.get_calender_spots():
            spot_id_array.append(spot.spot_id)
        return spot_id_array

    def get_spots(self,array_days): # orderd means array that consists of 5 arrays
        ordered_array =[]


        #array_slot_hours = ['08-09','09-10','10-11','11-12','12-13']
        array_slot_hours = ['18-19', '19-20', '20-21', '21-22', '22-23']
        #array_slot_hours = ['18-19', '19-20', '20-21', '21-22', '22-23']

        for hour in array_slot_hours:
            hour_array = []
            for day in array_days:
                for spot in self.calender_spot_set.all():
                    if spot.spot_id == (hour + ':' + day):
                        hour_array.append(spot)
            if not len(hour_array) == 0:
                ordered_array.append(hour_array)
        #print  ordered_array
        return ordered_array

    def __str__(self):
        return str(self.website_name) + ' - ' + str(self.website_placement)

class Calender_spot(models.Model):
    My_Calender     = models.ForeignKey(My_Calender, on_delete=models.CASCADE)
    spot_id         = models.CharField(max_length=250) #0day/mounth/hour  #08-09:27-08
    status          = models.CharField(max_length=250,default='open') # open/closed/bid(You are not the  only bidder )
    duration        = models.CharField(max_length=250)
    start_time      = models.CharField(max_length=250)
    ad_image        = models.CharField(max_length=250)

    def __str__(self):
        return str(self.My_Calender) + str(self.spot_id)

