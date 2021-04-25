from django.shortcuts import render, redirect
import random
import pytz
from datetime import datetime
from pytz import timezone


def index(request):
    if "gold" not in request.session or "activities" not in request.session:
        request.session["gold"] = 0
        request.session["activities"] = []
    context = {
        "activities": request.session["activities"]
    }
    return render(request, "index.html", context)  # add context


def process_money(request):
    if request.method == "POST":
        totalGold = request.session["gold"]
        location = request.POST["location"]
        activities = request.session["activities"]
        if location == "farm":
            goldChange = random.randint(10, 20)
        elif location == "cave":
            goldChange = random.randint(5, 10)
        elif location == "house":
            goldChange = random.randint(2, 5)
        else:
            goldChange = random.randint(-50, 50)
        totalGold += goldChange
        request.session["gold"] = totalGold
        # dates
        date_format = "%m/%d/%Y at %H:%M:%S %Z"
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone("US/Pacific"))
        myTime = date.strftime(date_format)
        if location == "casino":
            if goldChange >= 0:
                str = f"Entered a casino and won {goldChange} gold... Yay! ({myTime})"
            else:
                goldChange *= -1
                str = f"Entered a casino and lost {goldChange} gold... Ouch...({myTime})"
        else:
            str = f"Earned {goldChange} gold from the {location}! ({myTime})"
        activities.insert(0, str)
        request.session["activities"] = activities

    return redirect("/")
