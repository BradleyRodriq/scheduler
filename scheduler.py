#!/usr/bin/python3

import random

def generate_schedule(shifts_per_day, days, guides, guide_availability):
    shift_names = ["RFBB Guide 1", "RFBB Guide 2", "RFO 10:00 Guide 1", "RFO 10:00 Guide 2", "RFO 10:30 Guide 1", "RFO 10:30 Guide 2"]
    schedule = {day[0] if isinstance(day, tuple) else day: {shift_names[i]: None for i in range(shifts_per_day)} for day in days}

    for day in days:
        if isinstance(day, tuple):
            day, num_shifts = day
        else:
            num_shifts = shifts_per_day
        scheduled_guides = set()  # Keep track of guides already scheduled for this day
        for i in range(shifts_per_day):
            shift_key = shift_names[i]
            # Skip RFBB Guide 1 and RFBB Guide 2 on Sundays
            if day == "Sunday" and i in (0, 1):
                continue
            candidates = [guide for guide in guides
                          if guide_availability[guide].get(day, False)
                          and guide_availability[guide].get(shift_key, False)
                          and guide_availability[guide]['max_shifts'] > 0
                          and guide not in scheduled_guides]
            if not candidates:
                print(f"No candidates available for Day: {day}, Shift: {shift_key}")
                continue
            selected_guide = random.choice(candidates)
            schedule[day][shift_key] = selected_guide
            guide_availability[selected_guide]['max_shifts'] -= 1
            scheduled_guides.add(selected_guide)

    return schedule

shifts_per_day = 6
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ("Sunday", 4)]

guides = ["Amauri", "Paola", "Bradley", "Rene", "Danny", "Jean", "Kathy", "Nixshia", "Natalia"]

guide_availability = {
    "Amauri": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": True, "Saturday": True, "Sunday": True,
               "RFBB Guide 1": True, "RFBB Guide 2": False, "RFO 10:00 Guide 1": False, "RFO 10:00 Guide 2": False, "RFO 10:30 Guide 1": False, "RFO 10:30 Guide 2": False, 'max_shifts': 4},
    "Paola": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": True, "Saturday": True, "Sunday": True,
              "RFBB Guide 1": False, "RFBB Guide 2": True, "RFO 10:00 Guide 1": True, "RFO 10:00 Guide 2": True, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 5},
    "Bradley": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": False, "Saturday": True, "Sunday": True,
                "RFBB Guide 1": False, "RFBB Guide 2": True, "RFO 10:00 Guide 1": True, "RFO 10:00 Guide 2": True, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 5},
    "Rene": {"Monday": True, "Tuesday": True, "Wednesday": False, "Thursday": False, "Friday": False, "Saturday": False, "Sunday": True,
             "RFBB Guide 1": False, "RFBB Guide 2": True, "RFO 10:00 Guide 1": True, "RFO 10:00 Guide 2": True, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 3},
    "Danny": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": True, "Saturday": True, "Sunday": True,
              "RFBB Guide 1": False, "RFBB Guide 2": True, "RFO 10:00 Guide 1": True, "RFO 10:00 Guide 2": True, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 5},
    "Jean": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": True, "Saturday": True, "Sunday": True,
             "RFBB Guide 1": False, "RFBB Guide 2": True, "RFO 10:00 Guide 1": False, "RFO 10:00 Guide 2": True, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 5},
    "Kathy": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": True, "Saturday": True, "Sunday": True,
              "RFBB Guide 1": False, "RFBB Guide 2": True, "RFO 10:00 Guide 1": False, "RFO 10:00 Guide 2": True, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 5},
    "Nixshia": {"Monday": True, "Tuesday": True, "Wednesday": True, "Thursday": True, "Friday": True, "Saturday": True, "Sunday": True,
                "RFBB Guide 1": True, "RFBB Guide 2": True, "RFO 10:00 Guide 1": True, "RFO 10:00 Guide 2": True, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 5},
    "Natalia": {"Monday": False, "Tuesday": False, "Wednesday": False, "Thursday": False, "Friday": False, "Saturday": True, "Sunday": True,
                 "RFBB Guide 1": False, "RFBB Guide 2": False, "RFO 10:00 Guide 1": False, "RFO 10:00 Guide 2": False, "RFO 10:30 Guide 1": True, "RFO 10:30 Guide 2": True, 'max_shifts': 1}
}

randomized_schedule = generate_schedule(shifts_per_day, days_of_week, guides, guide_availability)

for day, shifts in randomized_schedule.items():
    if isinstance(day, tuple):
        day, num_shifts = day
    print(f"{day}:")
    for shift, guide in shifts.items():
        if guide is not None:
            print(f"  {shift}: {guide}")
        else:
            print(f"  {shift}: No guide available")
