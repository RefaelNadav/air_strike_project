
import requests
import json

lst_cities = ["Tehran", "Baghdad", "Damascus", "Kabul", "Sanaa", "Riyadh", "Cairo", "Beirut", "Amman", \
                  "Tripoli", "Khartoum", "Mosul", "Fallujah", "Kandahar", "Marrakesh"]

# location_data = []
dict_data_targets = {}
for city in lst_cities:
    url_location = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=cfea5411793c14999b71203d32b5d922"
    response_location = requests.get(url_location)
    data_location = response_location.json()

    dict_location = {
        "lat": data_location[0]["lat"],
        "lon": data_location[0]["lon"]
    }

    url_weather = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=cfea5411793c14999b71203d32b5d922"
    response_weather = requests.get(url_weather)
    data_weather = response_weather.json()

    tonight = list(filter(lambda x: x["dt_txt"][-8::] == "00:00:00", data_weather["list"]))

    if tonight:
        tonight_dct = tonight[0]

        dct_weather = {
            "main": tonight_dct["weather"][0]["main"],
            "clouds": tonight_dct["clouds"]["all"],
            "wind_speed": tonight_dct["wind"]["speed"],
            "dt_txt": tonight_dct["dt_txt"]
        }

        # dict_city = {city: dct_weather}
        # weather_data.append(dict_city)


    with open('targets.json', 'r') as file:
        targets = json.load(file)


    # for taget in targets:
    #     dict_data_targets[taget["City"]] = {
    #         'priority': taget['Priority'],
    #         'location': dict_location,
    #         'weather': dct_weather
    #     }

    for target in targets:
        if target["City"] == city:
            dict_data_targets[city] = {
                'priority': target['Priority'],
                'location': dict_location,
                'weather': dct_weather
            }
            break

with open("targets_data.json", 'w', encoding='utf-8') as file:
    json.dump(dict_data_targets, file, ensure_ascii=False, indent=4)



    # location_data.append(dict_location)




# weather_data = []
# for city in lst_cities:
#     url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=cfea5411793c14999b71203d32b5d922"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#
#         tonight = list(filter(lambda x: x["dt_txt"][-8::] == "00:00:00", data["list"]))
#
#         if tonight:
#             tonight_dct = tonight[0]
#
#             dct_weather = {
#                 "main": tonight_dct["weather"][0]["main"],
#                 "clouds": tonight_dct["clouds"]["all"],
#                 "wind_speed": tonight_dct["wind"]["speed"],
#                 "dt_txt": tonight_dct["dt_txt"]
#             }
#
#             dict_city = {city: dct_weather}
#             weather_data.append(dict_city)
#         else:
#             print(f"No data found for {city} at 2024-09-13 00:00:00")
#     else:
#         print(f"Failed to retrieve data for {city}. Status code: {response.status_code}")
#
# with open("targets_weather.json", 'w', encoding='utf-8') as file:
#     json.dump(weather_data, file, ensure_ascii=False, indent=4)
#
# print("Data successfully saved to ")

# url = "http://api.openweathermap.org/geo/1.0/direct?q=teheran&appid=cfea5411793c14999b71203d32b5d922"
# params = {'userId':1}

# response = requests.get(url)
# print(f"reponse is {response.json()}")
#
#
# url = "https://google.com"
#
# response = requests.get(url)
# print(f"reponse is {response.text}")