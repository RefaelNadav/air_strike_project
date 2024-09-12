from pilot import Pilot
from aircraft import Aircraft
from target import Target

from calculate_distance import calc_distance
from calculate_weights import *

from my_json import get_data

# print(get_data.get_pilots())
pilots = get_data.get_pilots()

pilot_objects = [Pilot(pilot['name'], pilot['skill_level']) for pilot in pilots]

aircrafts = get_data.get_aircrafts()
print(aircrafts)

aircrafts_objects = [Aircraft(aircraft['type'], aircraft['speed'], aircraft['fuel_capacity']) for aircraft in aircrafts]

# print(aircrafts_objects)

targets = get_data.get_targets()
print(targets)
# targets_objects = [Target(list(target.keys())[0], target['priority'], target['location'], target['weather']) for target in targets]
# print(targets_objects)

targets_objects = [Target(city, data['priority'], data['location'], data['weather']) for city, data in targets.items()]

lst_options = []
for target in targets_objects:
    distance = calc_distance(target)
    fit_score_target = weight_priority(target) + weight_weather(target) + weight_distance(distance)



    for pilot in pilot_objects:
        fit_score_pilot = fit_score_target + weight_pilot(pilot)


        for aircraft in aircrafts_objects:
            fit_score_total = fit_score_pilot + weight_aircraft(aircraft)

            lst_options.append((target.city_name, target.priority, pilot.name, aircraft.type, fit_score_total))


print(lst_options)
print(len(lst_options))



# for pilot in pilot_objects:
#     print(weight_pilot(pilot))
#
# for aircraft in aircrafts_objects:
#     print(weight_aircraft(aircraft))



