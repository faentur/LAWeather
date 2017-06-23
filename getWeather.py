#!/usr/bin/python

import requests

class WeatherChecker(object):
    def get_json(self, cityCode):
        """ gets the json response from api.openweathermap.org for the requested city code, returns as dict """
        r=requests.get("http://api.openweathermap.org/data/2.5/weather?id=3882428&APPID=c10bf994eac740d6c174f01adb18d2c4&units=imperial")

        return r.json()         # requests json() function returns a dictionary. beautifully simple

    def print_weather(self, data):
        """ prints out the weather, calling the dictionary objects directly from the dictionary. """
        print("The current temperature in %s is %s, with humidity at %s percent.\n" % (data['name'],data['main']['temp'],data['main']['humidity']))
        print("Wind is coming from the %s at %s miles per hour." % (self.wind_direction(data['wind']['deg']),data['wind']['speed']))
        print("Weather is currently %s." % data['weather'][0]['description'])

    def wind_direction(self, degree):
        """ gets the wind direction from its degrees. """
        dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE","S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        ix = int(degree/22.5)       # 360 degrees / 16 directions is 22.5
        return dirs[ix % 16]


if __name__ == '__main__':
    LACityCode = "3882428"          # if we were going to expand this, I'd use OptionParser to get command line input,
                                    # open the citylist.json file and do some searching to get ids from city names. Beyond the scope 
                                    # of what was requested, in this case.

    try:
        weather = WeatherChecker()
        weatherData = weather.get_json(LACityCode)
        weather.print_weather(weatherData)
    except:
        print("There's trouble in River City.")
