
import json

aircrafts = [
  {
    "type": "F-16",
    "speed": 2400,
    "fuel_capacity": 5000
  },
  {
    "type": "F-35",
    "speed": 3000,
    "fuel_capacity": 6000
  },
  {
    "type": "MiG-29",
    "speed": 2450,
    "fuel_capacity": 4500
  },
  {
    "type": "Su-27",
    "speed": 2500,
    "fuel_capacity": 5200
  },
  {
    "type": "Eurofighter Typhoon",
    "speed": 2495,
    "fuel_capacity": 5600
  },
  {
    "type": "Rafale",
    "speed": 2130,
    "fuel_capacity": 4700
  },
  {
    "type": "F/A-18",
    "speed": 1915,
    "fuel_capacity": 4900
  }
]

with open('aircraft.json', 'w') as file:
  json.dump(aircrafts, file)






pilots = [
  {
    "name": "John Doe",
    "skill_level": 8
  },
  {
    "name": "Jane Smith",
    "skill_level": 6
  },
  {
    "name": "Michael Johnson",
    "skill_level": 7
  },
  {
    "name": "Emily Davis",
    "skill_level": 9
  },
  {
    "name": "Robert Brown",
    "skill_level": 5
  },
  {
    "name": "Sarah Wilson",
    "skill_level": 8
  },
  {
    "name": "David Lee",
    "skill_level": 6
  },
  {
    "name": "Chris Walker",
    "skill_level": 7
  },
  {
    "name": "Jessica Miller",
    "skill_level": 10
  },
  {
    "name": "Daniel Harris",
    "skill_level": 4
  }
]


with open('pilots.json', 'w') as file:
    json.dump(pilots, file)

targets = [
  {
    "City": "Tehran",
    "Priority": 5
  },
  {
    "City": "Baghdad",
    "Priority": 5
  },
  {
    "City": "Damascus",
    "Priority": 5
  },
  {
    "City": "Kabul",
    "Priority": 4
  },
  {
    "City": "Sanaa",
    "Priority": 4
  },
  {
    "City": "Riyadh",
    "Priority": 4
  },
  {
    "City": "Cairo",
    "Priority": 3
  },
  {
    "City": "Beirut",
    "Priority": 3
  },
  {
    "City": "Amman",
    "Priority": 3
  },
  {
    "City": "Tripoli",
    "Priority": 2
  },
  {
    "City": "Khartoum",
    "Priority": 2
  },
  {
    "City": "Mosul",
    "Priority": 2
  },
  {
    "City": "Fallujah",
    "Priority": 1
  },
  {
    "City": "Kandahar",
    "Priority": 1
  },
  {
    "City": "Marrakesh",
    "Priority": 1
  }
]

with open('targets.json', 'w') as file:
  json.dump(targets, file)
