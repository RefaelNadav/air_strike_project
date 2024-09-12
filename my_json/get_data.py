
import json

file_targets_path = 'C:/Users/rn385\PycharmProjects/air_strike_project/my_json/targets_data.json'
with open(file_targets_path, 'r') as file:
    targets = json.load(file)

def get_targets():
    return targets

file_pilots_path = 'C:/Users/rn385\PycharmProjects/air_strike_project/my_json/pilots.json'
with open(file_pilots_path, 'r') as file:
    pilots = json.load(file)
def get_pilots():

    return pilots

file_aircrafts_path = 'C:/Users/rn385\PycharmProjects/air_strike_project/my_json/aircraft.json'
with open(file_aircrafts_path, 'r') as file:
    aircrafts = json.load(file)
def get_aircrafts():

    return aircrafts
