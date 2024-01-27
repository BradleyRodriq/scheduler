#!/usr/bin/python3

import random

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

shifts_weekdays = ["RFBB", "RF1", "RF2"]
shifts_sunday = ["RF Only 1", "RF Only 2"]

guides = ["Amauri", "Paola", "Bradley", "Rene", "Jean",
          "Kathy", "Nixshia", "Natalia", "Danny"]

guide_max = {"Amauri": 4, "Paola": 5, "Bradley": 5, "Rene": 3, "Jean": 5,
            "Kathy": 5, "Nixshia": 5, "Natalia": 1, "Danny": 5}

guide_days = {guide: 0 for guide in guides}

schedule = {day: {shift: {"Guide 1": "", "Guide 2": ""}
                for shift in shifts_weekdays} for day in days[:6]}

schedule["Sunday"] = {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_sunday}

random_guide = random.choice(guides)
guide_days[random_guide] += 1
random_day = random.choice(days)
random_shift = random.choice(shifts_weekdays)

availability = {guide: {day: {shift: {"Guide 1": True, "Guide 2": True} for shift in shifts_weekdays} for day in days[:6]}for guide in guides}

availability["Bradley"]["Friday"] = False
availability["Amauri"]["Sunday"] = False
availability["Rene"]["Wednesday"] = False
availability["Rene"]["Thursday"] = False
availability["Rene"]["Friday"] = False
availability["Rene"]["Saturday"] = False
availability["Natalia"]["Monday"] = False
availability["Natalia"]["Tuesday"] = False
availability["Natalia"]["Wednesday"] = False
availability["Natalia"]["Thursday"] = False
availability["Natalia"]["Friday"] = False

for guide in ["Bradley", "Paola", "Jean", "Rene", "Danny", "Natalia", "Kathy", "Rene"]:
    for day in days[:6]:
        for shift in shifts_weekdays:
            availability[guide][day]["RFBB"] = False
for guide in ["Jean", "Kathy"]:
    for day in days[:6]:
        for shift in shifts_weekdays:
            availability[guide][day]["RF Only 1"] = False
for guide in ["Jean", "Kathy"]:
    for shift in shifts_sunday:
        availability[guide][day]["RF Only 1"] = False

amauri_days = 0
bradley_days = 0
paola_days = 0
rene_days = 0
jean_days = 0
kathy_days = 0
nixshia_days = 0
natalia_days = 0
danny_days = 0

for day in days:
    print(f"{day}:")
    print()
    for shift, guides in schedule[day].items():
        guide_1 = guides["Guide 1"] if guides["Guide 1"] else "None"
        guide_2 = guides["Guide 2"] if guides["Guide 2"] else "None"
        print(f"  {shift}: Guide 1: {guide_1}, Guide 2: {guide_2}")
        