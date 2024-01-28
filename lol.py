#!/usr/bin/python3

import random

def initialize_schedule():
    return {day: {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_weekdays} for day in days[-6:]}

def initialize_sunday_schedule():
    return {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_sunday}

def initialize_availability():
    return {guide: {day: {shift: {"Guide 1": "", "Guide 2": ""} for shift in shifts_weekdays + shifts_sunday} for day in days} for guide in guides}

def mark_unavailable_days():
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

def mark_shift_unavailable(guides_list, days_list, shift):
    for guide in guides_list:
        for day in days_list:
            if shift == availability[guide][day]:
                availability[guide][day][shift]['Guide 1'] = False

def print_schedule():
    for day in days:
        print(f"{day}:")
        for shift, guides in schedule[day].items():
            guide_1 = guides["Guide 1"] if guides["Guide 1"] else "None"
            guide_2 = guides["Guide 2"] if guides["Guide 2"] else "None"
            print(f"  {shift}: Guide 1: {guide_1}, Guide 2: {guide_2}")
        print()

# Global variables
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
shifts_weekdays = ["RFBB", "RF1", "RF2"]
shifts_sunday = ["RF1", "RF2"]
guides = ["Amauri", "Paola", "Bradley", "Rene", "Jean", "Kathy", "Nixshia", "Natalia", "Danny"]
availability = initialize_availability()
schedule = initialize_schedule()

def main():
    random_guide = random.choice(guides)
    mark_unavailable_days()
    mark_shift_unavailable(["Bradley", "Paola", "Jean", "Rene", "Danny", "Natalia", "Kathy", "Rene"], days[-6:], shifts_weekdays[0])
    mark_shift_unavailable(["Jean", "Kathy"], ["Sunday"], shifts_sunday[0])
    
    for day in days[-6:]:
        schedule[day] = initialize_schedule()[day]
    
    for day in days:
        print_schedule()

if __name__ == "__main__":
    main()