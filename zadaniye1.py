import pyowm
import datetime
print('zadaniye1')
owm = pyowm.OWM('1324966e672503c5950979c2899c9350')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()
translate = {'Rostov-on-Don': 'Ростов-на-Дону', 'RU': 'Россия'}
print(weather.get_clouds())
def WhatIsCloudness():
    if 0<=weather.get_clouds()<=10:
        return 'солнечная'
    if 10<weather.get_clouds()<=30:
        return 'немного облачная'
    if 30<weather.get_clouds()<=70:
        return 'пасмурная'
    if 70<weather.get_clouds()<=100:
        return 'мрачная'
def WhatIsWind():
    if 0<weather.get_wind()['deg']<=90:
        return 'северо-восточный'
    if 90<weather.get_wind()['deg']<=180:
        return 'юго-восточный'
    if 180<weather.get_wind()['deg']<=270:
        return 'юго-западный'
    if 270<weather.get_wind()['deg']<=360:
        return 'северо-западный'
print('Погода в городе ' + translate[location.get_name()] +'(' + translate[location.get_country()] + ') ' +
str(WhatIsCloudness()) + ', на сегодня в ' + datetime.datetime.now().strftime("%H:%M") + ' облачность составляет ' +
str(weather.get_clouds()) + ', давление ' + str(weather.get_pressure()['press']) + ' мм. рт. ст ' + ' температура ' +
str(weather.get_temperature('celsius')['temp']) + ' градусов Цельсия, ' + 'ночью - ' +
str(weather.get_temperature('celsius')['temp_min']) + ', днём - ' + str(weather.get_temperature('celsius')['temp_max']) +
', ветер ' + str(WhatIsWind()) + ', ' + str(weather.get_wind()['speed']) + 'м/c')

