#!/usr/bin/python3

import random

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

shifts_weekdays = ["RFBB", "RF1", "RF2"]
shifts_sunday = ["RF1", "RF2"]

guides = ["Amauri", "Paola", "Bradley", "Rene", "Jean",
          "Kathy", "Nixshia", "Natalia", "Danny"]

guide_max = {"Amauri": 4, "Paola": 5, "Bradley": 5, "Rene": 3, "Jean": 5,
            "Kathy": 5, "Nixshia": 5, "Natalia": 1, "Danny": 5}

guide_days = {guide: 0 for guide in guides}

availability = {
    guide: {
        day: {
            shift: {"Guide 1": True, "Guide 2": True}
            for shift in shifts_weekdays + shifts_sunday
        }
        for day in days
    }
    for guide in guides
}

availability["Bradley"]["Friday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Amauri"]["Sunday"][shifts_sunday[0]]['Guide 1'] = False
availability["Rene"]["Wednesday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Rene"]["Thursday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Rene"]["Friday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Rene"]["Saturday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Natalia"]["Monday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Natalia"]["Tuesday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Natalia"]["Wednesday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Natalia"]["Thursday"][shifts_weekdays[0]]['Guide 1'] = False
availability["Natalia"]["Friday"][shifts_weekdays[0]]['Guide 1'] = False

for guide in ["Bradley", "Paola", "Jean", "Rene", "Danny", "Natalia", "Kathy", "Rene"]:
    for day in days[-6:]:
        availability[guide][day][shifts_weekdays[0]]['Guide 1'] = False

for guide in ["Jean", "Kathy"]:
    for day in ["Sunday"]:
        availability[guide][day][shifts_sunday[0]]['Guide 1'] = False


schedule = {day: {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_weekdays} for day in days[-6:]}
schedule["Sunday"] = {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_sunday}

for day in days:
    print(f"{day}:")
    for shift, guides_info in schedule[day].items():
        if guides_info["Guide 1"]:
            guide_1 = guides_info["Guide 1"]
            availability_info = availability[guide_1][day][shift]['Guide 1']
            if availability_info:
                selected_guide = guide_1
                schedule[day][shift]['Guide 1'] = selected_guide
                guide_days[selected_guide] += 1
                availability[selected_guide][day][shift]['Guide 1'] = False
            else:
                selected_guide = "None"
        else:
            selected_guide = "None"
        
        guide_2 = guides_info["Guide 2"] if guides_info["Guide 2"] else "None"
        print(f"  {shift}: Guide 1: {selected_guide}, Guide 2: {guide_2}")
    print()

