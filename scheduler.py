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

while True:
    if (
        amauri_days >= 4 and
        bradley_days >= 5 and
        paola_days >= 5 and
        renee_days >= 3 and
        jean_days >= 5 and
        kathy_days >= 5 and
        nixshia_days >= 5 and
        natalia_days >= 1
    ):
        break

    random_day = random.choice(days)
    
    if random_day != "Sunday":
        random_shift = random.choice(shifts_weekdays)
    else:
        random_shift = random.choice(shifts_sunday)

    assigned_guides = set()
    assigned_guides.add(schedule[random_day][random_shift]["Guide 1"])
    assigned_guides.add(schedule[random_day][random_shift]["Guide 2"])

    available_guides = [guide for guide in guides if guide not in assigned_guides]

    if available_guides:
        guide = random.choice(available_guides)

        if (
            (guide == "Amauri" and amauri_days < 4 and random_shift == "RFBB" and schedule[random_day]['RFBB']["Guide 1"] == "") or
            (guide == "Nixshia" and nixshia_days < 5 and random_shift == "RFBB" and schedule[random_day]['RFBB']["Guide 1"] == "") or
            (guide == "Natalia" and natalia_days < 1 and random_day in ["Saturday", "Sunday"] and random_shift != "RFBB") or
            (guide == "Bradley" and bradley_days < 5 and random_day != "Friday" and random_shift != "RFBB") or
            (guide == "Paola" and paola_days < 5 and random_shift != "RFBB") or
            (guide == "Renee" and renee_days < 3 and random_day in ["Sunday", "Monday", "Tuesday"] and random_shift != "RFBB") or
            (guide == "Jean" and random_shift not in ["RFBB", "RF Only 1"])
        ):
            if random_shift == "RFBB" and schedule[random_day]['RFBB']["Guide 1"] == "":
                schedule[random_day]['RFBB']["Guide 1"] = guide
                if guide == "Amauri":
                    amauri_days += 1
                elif guide == "Nixshia":
                    nixshia_days += 1
            elif schedule[random_day][random_shift]["Guide 2"] == "":
                schedule[random_day][random_shift]["Guide 2"] = guide

            # Update days for each guide
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
                natalia_days += 1

# Print the schedule
for day in days:
    print(f"{day}:")
    for shift, guides in schedule[day].items():
        guide_1 = guides["Guide 1"] if guides["Guide 1"] else "None"
        guide_2 = guides["Guide 2"] if guides["Guide 2"] else "None"
        print(f"  {shift}: Guide 1: {guide_1}, Guide 2: {guide_2}")
