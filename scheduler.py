#!/usr/bin/python3
import random

# Define shifts and days
shifts = ["rfbb", "rf1", "rf2"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Define guides with their maximum days of work per week
guides_info = {
    "amauri": {"max_days_per_week": 5},
    "paola": {"max_days_per_week": 5},
    "bradley": {"max_days_per_week": 5},
    "rene": {"max_days_per_week": 3},
    "jean": {"max_days_per_week": 5},
    "danny": {"max_days_per_week": 5},
    "kathy": {"max_days_per_week": 5},
    "nixshia": {"max_days_per_week": 5},
    "natalia": {"max_days_per_week": 1},
}

# Initialize schedule
schedule = {day: {shift: {"guide1": None, "guide2": None} for shift in shifts} for day in days}

# Helper function to check if a guide is available on a given day and shift
def is_guide_available(day, shift, guide):
    return schedule[day][shift]["guide1"] != guide and schedule[day][shift]["guide2"] != guide

# Helper function to check if a guide has reached the maximum days of work per week
def can_work_more(guide):
    scheduled_days = sum(1 for day in days for shift in shifts if schedule[day][shift]["guide1"] == guide or schedule[day][shift]["guide2"] == guide)
    return scheduled_days < guides_info[guide]["max_days_per_week"]

# Randomize schedule
random_day = random.choice(days)
for day in days:
    for shift in shifts:
        if random_day == "Sunday" and shift in ["rf only 1", "rf only 2"]:
            available_guides = [guide for guide in guides_info.keys() if is_guide_available(day, shift, guide) and can_work_more(guide)]
            if available_guides:
                guide1 = random.choice(available_guides)
                available_guides.remove(guide1)
                guide2 = random.choice(available_guides)
                schedule[day][shift]["guide1"] = guide1
                schedule[day][shift]["guide2"] = guide2
        else:
            available_guides = [guide for guide in guides_info.keys() if is_guide_available(day, shift, guide) and can_work_more(guide)]
            if available_guides:
                if shift == "rfbb" and schedule[random_day][shift]["guide1"] is None:
                    if "amauri" in available_guides:
                        guide1 = "amauri"
                        available_guides.remove("amauri")
                        guide2 = random.choice(available_guides)
                        schedule[day][shift]["guide1"] = guide1
                        schedule[day][shift]["guide2"] = guide2
                    elif "nixshia" in available_guides:
                        guide1 = "nixshia"
                        available_guides.remove("nixshia")
                        guide2 = random.choice(available_guides)
                        schedule[day][shift]["guide1"] = guide1
                        schedule[day][shift]["guide2"] = guide2
                elif shift == "rfbb" and schedule[day][shift]["guide1"] != "amauri":
    # Nixshia always covers the other rfbb guide 1 shift when Amauri is not scheduled
                    if "nixshia" in available_guides:
                        guide1 = "nixshia"
                        available_guides.remove("nixshia")
                        guide2 = random.choice(available_guides)
                        schedule[day][shift]["guide1"] = guide1
                        schedule[day][shift]["guide2"] = guide2

                elif shift != "rfbb" and schedule[day][shift]["guide1"] or schedule[day][shift]["guide2"]:
                    # Danny can work in rfbb other than guide 1
                    available_guides.remove("danny")
                    guide1 = "danny"
                    guide2 = random.choice(available_guides)
                    schedule[day][shift]["guide1"] = guide1
                    schedule[day][shift]["guide2"] = guide2
                elif shift != "rfbb" and schedule[day][shift]["guide2"] in ["jean", "kathy"]:
                    # Jean and Kathy can only work as guide 2
                    guide1 = random.choice(available_guides)
                    available_guides.remove(guide1)
                    guide2 = "jean" if "jean" in available_guides else "kathy"
                    schedule[day][shift]["guide1"] = guide1
                    schedule[day][shift]["guide2"] = guide2
                else:
                    guide1 = random.choice(available_guides)
                    available_guides.remove(guide1)
                    guide2 = random.choice(available_guides)
                    schedule[day][shift]["guide1"] = guide1
                    schedule[day][shift]["guide2"] = guide2

# Print the schedule
for day in days:
    print()
    print(f"{day}")
    for shift in shifts:
        print(f"    {shift}:")
        print(f"        Guide 1: {schedule[day][shift]['guide1']}") 
        print(f"        Guide 2: {schedule[day][shift]['guide2']}")
        