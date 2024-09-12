
from pilot import Pilot
from aircraft import Aircraft
from target import Target

def weight_distance(distance):

    if distance > 4000:
        return 0
    elif distance > 3000:
        return 5
    elif distance > 2000:
        return 10
    elif distance > 1000:
        return 15
    else:
        return 20

def weight_priority(target: Target):
    return target.priority * 4

def weight_aircraft(aircraft: Aircraft):
    fuel_capacity = aircraft.fuel_capacity
    speed = aircraft.speed
    result = 0
    if speed > 3000:
        result += 10
    elif speed > 2500:
        result += 7.5
    elif speed > 2200:
        result += 5
    elif speed > 2000:
        result += 2.5

    if fuel_capacity > 6000:
        return result + 10
    if fuel_capacity > 5200:
        return result + 7.5
    if fuel_capacity > 4900:
        return result + 5
    if fuel_capacity > 4600:
        return result + 2.5
    return result


def weight_weather(target: Target):
    result = 0
    weather = target.weather
    if weather["main"] == "Clear":
        result += 7
    elif weather["main"] == "Clouds":
        result += 5
    elif weather["main"] == "Rain":
        result += 3
    elif weather["main"] == "Stormy":
        result += 1

    if weather["clouds"] == 0:
        result += 7
    elif weather["clouds"] < 25:
        result += 5
    elif weather["clouds"] < 50:
        result += 3
    elif weather["clouds"] < 75:
        result += 1

    if weather['wind_speed'] < 1:
        return result + 6
    if weather['wind_speed'] < 5:
        return result + 4
    if weather['wind_speed'] < 10:
        return result + 2
    if weather['wind_speed'] < 15:
        return result + 1
    return result

def weight_pilot(pilot: Pilot):
    return pilot.skill * 2





