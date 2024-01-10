import requests
from django.shortcuts import render
from django.conf import settings


def home(request):
    api_key = settings.API_KEY

    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather(api_key, city)
        context = {'weather_data': weather_data, 'city': city}
    else:
        default_city = 'Delhi'
        weather_data = get_weather(api_key, default_city)
        context = {'weather_data': weather_data, 'city': default_city}

    return render(request, 'weather_app/index.html', context)


def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data
