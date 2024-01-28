#!/usr/bin/python3

import random

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

shifts_weekdays = ["RFBB", "RF1", "RF2"]
shifts_sunday = ["RF1", "RF2"]

guides = ["Amauri", "Paola", "Bradley", "Rene", "Jean",
          "Kathy", "Nixshia", "Natalia", "Danny"]

guide_max = {"Amauri": 4, "Paola": 5, "Bradley": 5, "Rene": 3, "Jean": 5,
            "Kathy": 5, "Nixshia": 5, "Natalia": 1, "Danny": 5}

amauri_days = 0
bradley_days = 0
paola_days = 0
rene_days = 0
jean_days = 0
kathy_days = 0
nixshia_days = 0
natalia_days = 0
danny_days = 0

guide_days = {guide: 0 for guide in guides}

schedule = {day: {shift: {"Guide 1": "", "Guide 2": ""}
                for shift in shifts_weekdays} for day in days[-6:]}

schedule["Sunday"] = {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_sunday}

availability = {guide: {day: {shift: {"Guide 1": True, "Guide 2": True}for shift in shifts_weekdays + shifts_sunday
            }for day in days}for guide in guides}


for day in days:
    print(f"{day}:")
    for shift, guides in schedule[day].items():
        guide_1 = guides["Guide 1"] if guides["Guide 1"] else "None"
        guide_2 = guides["Guide 2"] if guides["Guide 2"] else "None"
        print(f"  {shift}: Guide 1: {guide_1}, Guide 2: {guide_2}")
    print()
        