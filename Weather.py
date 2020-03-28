#Made by xylla#7803 on Discord

import requests
import pytz
import datetime

location = requests.get('http://ip-api.com/json').json()
sun_times = requests.get(f"https://api.sunrise-sunset.org/json?lat={location['lat']}&lng={location['lon']}").json()
weather = requests.get(f"https://api.darksky.net/forecast/44f2b99a7255b32ca0a338aa257965ca/{location['lat']},{location['lon']}").json()

timezone = location['timezone']

time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

temp = weather['currently']['temperature']
het = weather['daily']['data'][0]['temperatureHigh']
let = weather['daily']['data'][0]['temperatureLow']
temperature = f"{round((int(temp) - 32) * 5 / 9)} °C | {round(int(temp))} °F"
highest_temperature = f"{round((int(het) - 32) * 5 / 9)} °C | {round(int(het))} °F"
lowest_temperature = f"{round((int(let) - 32) * 5 / 9)} °C | {round(int(let))} °F"

weather_summary = weather['currently']['summary']
wind_speed = f"{round(int(weather['currently']['windSpeed']) * 1.60934, 2)} km/h | {weather['currently']['windSpeed']} mph"

if int(weather['currently']['windSpeed']) == 0:
    wind_direction = '--'
else:
    def degrees_to_cardinal(degrees):
        dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE""S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        ix = int((degrees + 11.25) / 22.5)
        return dirs[ix % 16]

    wind_direction = f"{weather['currently']['windBearing']}° {degrees_to_cardinal(int(weather['currently']['windSpeed']))}"

cloud_coverage = weather['currently']['cloudCover']
weather_later = weather['daily']['data'][0]['summary'].replace('.', '')

day_Length = sun_times['results']['day_length'][:5]
srt = weather['daily']['data'][0]['sunriseTime']
sst = weather['daily']['data'][0]['sunsetTime']
sunrise = datetime.datetime.fromtimestamp(int(srt), tz=pytz.timezone(location['timezone'])).strftime("%H:%M")
sunset = datetime.datetime.fromtimestamp(int(sst), tz=pytz.timezone(location['timezone'])).strftime("%H:%M")

information = (f"\nWeather in {location['city']}, {location['country']} as of {time}\n\n"
               f"Current temperature: {temperature}\n"
               f"Highest estimated temperature: {highest_temperature}\n"
               f"Lowest estimated temperature: {lowest_temperature}\n\n"
               f"Weather: {weather_summary}\n"
               f"Wind Speed: {wind_speed}\n"
               f"Wind direction {wind_direction}\n"
               f"Cloud coverage: {cloud_coverage}\n"
               f"Upcoming weather: {weather_later}\n\n"
               f"Current day length: {day_Length}\n"
               f"Sunrise: {sunrise}\n"
               f"Sunset: {sunset}\n\n\n")

print(information[:-1])

data = input("Would you like to store this information?\nAnswer [Yes] or [No]\n\n>>>").lower()

if data in ['yes', 'ye', 'y', 'ok']:
    with open("Weather_Logs.txt", "a") as f:
        f.write(information[1:])
        print("\nInformation has been successfully stored.\nHave a great day, goodbye!")
else:
    print("\nHave a great day, goodbye!")