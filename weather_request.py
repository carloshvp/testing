import requests
import Secrets

url = "http://api.openweathermap.org/data/2.5/weather?q=Stuttgart&units=metric&appid=" + \
    Secrets.OpenWeatherAPPID
request = requests.get(url)

weather_json = request.json()
print(weather_json)
main_weather = weather_json["main"]
temp = str(main_weather["temp"])
print("The temperature in Stuttgart is " + temp)
