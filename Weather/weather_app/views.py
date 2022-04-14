from django.shortcuts import render
import urllib.request
import json
import random

# Create your views here.
def index(request):
        bg_options = ["sunny", "sunnyn", "cloudy"]
        index_bg = random.choice(bg_options)
        context = {"indexbg": str(index_bg)}

        return render(request, "weather_app/index.html", context)

def result(request):

    if request.method == "POST":
        city = request.POST['city']
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
    return render(request, "weather_app/result.html", context)