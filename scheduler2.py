#!/usr/bin/python3

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
shifts_weekdays = ["RFBB", "RF1", "RF2"]
shifts_sunday = ["RF Only 1", "RF Only 2"]
guides = ["Amauri", "Paola", "Bradley", "Renee", "Jean", "Kathy", "Nixshia", "Natalia"]

schedule = {day: {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_weekdays} for day in days[:6]}
schedule["Sunday"] = {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_sunday}

# Conditions
amauri_days = 0
bradley_days = 0
paola_days = 0
renee_days = 0
jean_days = 0
kathy_days = 0
nixshia_days = 0
natalia_days = 0
"""
if guide == "Bradley":
    bradley_days += 1
elif guide == "Paola":
    paola_days += 1
elif guide == "Renee":
    renee_days += 1
elif guide == "Jean":
    jean_days += 1
elif guide == "Kathy":
    kathy_days += 1
elif guide == "Nixshia":
    nixshia_days += 1
elif guide == "Natalia":
    natalia_days += 1 """

# Print the schedule
for day in days:
    print(f"{day}:")
    for shift, guides in schedule[day].items():
        guide_1 = guides["Guide 1"] if guides["Guide 1"] else "None"
        guide_2 = guides["Guide 2"] if guides["Guide 2"] else "None"
        print(f"  {shift}: Guide 1: {guide_1}, Guide 2: {guide_2}")