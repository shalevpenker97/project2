from django.http import HttpResponse
import calendar
from datetime import date,timedelta
import datetime
from django.shortcuts import render, get_object_or_404
from .models import My_Calender,Calender_spot
from music.models import Album
from django.http import HttpResponseRedirect
import json

#def index(request):
#    return HttpResponse('<h1>This is the calender home page</h1>')


def index(request, year=date.today().year, month=date.today().month):
    #In order to return a nice 08:00 -17:00 presentation to the calender
    hours =[]
    for x in range(8,17):
        hours.append(str(x)+':00 - '+str(x+1)+':00')


    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]

    #selsect all slots for this specific calender

    context = {
        'title':"MyClub Event Calendar - %s %s" % (month_name, year),
        'year': int(year),
        'month': int(month),
        'hours':hours,
        #'array':range(1,10)

    }
    return render(request, 'cal/index.html', context)

def detail(request):
    Calender = My_Calender.objects.all()[0]

    Calender.get_calender_spots()
    #This is for starting the calender in 'today' day
    dict_days ={}
    array_name_days = []
    array_day_id =[]
    for day in range(0,7):
        day_name = (calendar.day_name[(date.today() + timedelta(days=day)).weekday()])
        #print (day_name)
        day_id   = ((date.today() + timedelta(days=day)).strftime('%d')+'-'+(date.today() + timedelta(days=day)).strftime('%m'))
        #print (day_id)
        #array_name_days.append(calendar.day_name[(date.today() + timedelta(days=day)).weekday()]) # will extract the name in the week 'Sunday'
        #array_day_id.append((date.today() + timedelta(days=day)).strftime('%d')+'-'+(date.today() + timedelta(days=day)).strftime('%m'))
        dict_days[day_name]=day_id

   # print (list(dict_days.values()))

    #This will print the id of the slot:  23-08:08-09 / 23-08:09-10 / 23-08:10-11
    #array_slot_hours = ['08-09', '09-10', '10-11', '11-12', '12-13']
    #array_slot_hours =['13-14','14-15','15-16','16-17','17-18']
    array_slot_hours = ['18-19', '19-20', '20-21', '21-22', '22-23']

    #This will populate slots that doesnt exist
    for hour in array_slot_hours:
        hour_array = []
        for day in dict_days.values():
            if not Calender_spot.objects.filter(My_Calender=Calender,spot_id=(hour+':'+day)).exists():
                slot1 = Calender_spot(My_Calender=Calender, spot_id=(hour + ':' + day), status="open" , duration="1", start_time="1",
                                      ad_image="image1")
                slot1.save()

    #print (list(dict_days.values()))

    User_Albums = Album.objects.filter(user=request.user)

    #print (User_Albums[0].album_title)

    #print  (Calender.get_spots(dict_days.values()))
    #print (Calender.get_spots())
    #print ('calendar_final_2d_array' + str(type(calendar_final_2d_array[0][0])))



    #print (len(calendar_final_2d_array))
    ###array_08_09 = []
    #array1 =['23-08','24-08','','','','','']

    print (Calender.get_spots(list(dict_days.values())))
    context = {
        'Calender': Calender,
        'array_days': range(1, 8),
        'array_slots':range(1, 5),
        'array_name_days':array_name_days,
        'array_day_id':array_day_id,
        'dict_days':dict_days,
        'array_slot_hours':array_slot_hours,
        'calender_final_slots':Calender.get_spots(list(dict_days.values())),
        'User_Albums':User_Albums,
        'Calender_image':"/media/"+str(Calender.calender_image)
        #'calendar_final_2d_array':calendar_final_2d_array # This is an array od 5 arrays
        #'array_name_days': ['Sunday','Monday','Thuesday','Wednesday','Thursday','Friday','Saturday']
    }

    return render(request, 'cal/detail.html', context)

#return render(request, 'music/detail.html', {'album': album, 'user': user})
def bid(request):
    Calender = request.POST['Calender']
    Spot_id  = request.POST['spot_id']
    image    = request.POST['image']

    #body = json.loads(request.body)
    #print ("Name" + str(body['Name']))
    #print ("Phone:" +str(body['Phone']))
    print (request.POST['spot_id'])
    print (request.POST['Calender'])
    print (request.POST['image'])
    Calender_spot.objects.filter(My_Calender=Calender, spot_id=Spot_id).update(ad_image=image)
    #print ((request.body))
    return HttpResponse(status=200)
    #print (request.POST.copy())

def advertise(request):
    #Representation of the date and time (hour - date)

    day_id  =  str(date.today().strftime('%d'))+"-"+str(date.today().strftime('%m'))
    hour    =  str((datetime.datetime.now()+timedelta(hours=3)).hour)+"-"+str((datetime.datetime.now()+timedelta(hours=4)).hour)
    spot_id = str(hour)+":"+str(day_id)
    print (str(hour)+":"+str(day_id))
    image = str(Calender_spot.objects.filter(spot_id=spot_id).values_list("ad_image", flat=True))[2:-2]

    #print ('http://127.0.0.1:8000'+str(image))
    #'file:///Users/shalev.p/PycharmProjects/Viberr/media/s-l500_7.jpg'
    return HttpResponseRedirect('http://127.0.0.1:8000'+str(image))


def calenders(request):

    return render(request, 'cal/menu.html')

def testing(request):

    return render(request,'cal/testing.html')

def testing2(request):

    return render(request,'cal/testing2.html')

def spot_list(request, website):

    spot_list = My_Calender.objects.filter(website_name=website)

    context = { 'website': website,
                'spot_list':spot_list
    }
    return render(request,'cal/spot_list.html', context)