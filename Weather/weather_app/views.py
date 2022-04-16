from django.shortcuts import render
import urllib.request
import json
import random
from urllib.error import HTTPError
# Create your views here.
def index(request):
        bg_options = ["sunny", "sunnyn", "cloudy"]
        index_bg = random.choice(bg_options)
        context = {"indexbg": str(index_bg)}

        return render(request, "weather_app/index.html", context)

def result(request):

    if request.method == "POST":
        pre_city = request.POST['city']
        city = pre_city.replace(" ", "")
        print (city)
        print('----------------------')
        try:
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=ed446cc9022df49fe487d2ecacdc9d7d').read()
            data_list = json.loads(source)
           
            context = {
                "country": str(data_list['sys']['country']),
                "wind": str(round(data_list['wind']['speed'])),
                "feels": str(round(data_list['main']['feels_like'])),
                "temp": str(round(data_list['main']['temp'])),
                "humidity": str(round(data_list['main']['humidity'])),
                "description": str(data_list['weather'][0]['description']),
                "icon": data_list['weather'][0]['icon'],
                "city": city.title(),
                "color": "",
                "time": "",
                
            }

            if "clear sky" == context["description"] and "n" in context["icon"]:
                context["color"] = "sunnyn"
                context["time"] = "pm"
            elif "clear sky" == context["description"] and "d" in context["icon"]:
                context["color"] = "sunny"
                context["time"] = "am"
            elif "n" in context["icon"]:
                context["time"] = "pm"
                context["color"] = "cloudy"
            else:
                context["time"] = "am"
                context["color"] = "cloudy"
        except HTTPError as err:
            if err.code == 404:
                return render(request, "weather_app/error.html")
            
    return render(request, "weather_app/result.html", context)