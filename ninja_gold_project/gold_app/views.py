from django.shortcuts import render, redirect
import random
import pytz
from datetime import datetime
from pytz import timezone


def index(request):
    if "gold" not in request.session or "activities" not in request.session:
        # defines session variables if not already existing
        request.session["gold"] = 0
        request.session["activities"] = []
    context = {
        "activities": request.session["activities"]
    }
    return render(request, "index.html", context)


def process_money(request):
    if request.method == "POST":
        # Define session variables for ease of use
        totalGold = request.session["gold"]
        location = request.POST["location"]
        activities = request.session["activities"]
        # Assign random int to goldChange based on button pressed
        if location == "farm":
            goldChange = random.randint(10, 20)
        elif location == "cave":
            goldChange = random.randint(5, 10)
        elif location == "house":
            goldChange = random.randint(2, 5)
        else:
            goldChange = random.randint(-50, 50)
        # Update gold values
        totalGold += goldChange
        request.session["gold"] = totalGold
        # Define date formats
        date_format = "%m/%d/%Y at %H:%M:%S %Z"
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone("US/Pacific"))
        myTime = date.strftime(date_format)
        # Update str based on casino win/loss OR other building gains
        if location == "casino":
            if goldChange >= 0:
                str = f"Entered a casino and won {goldChange} gold... Yay! ({myTime})"
            else:
                goldChange *= -1
                str = f"Entered a casino and lost {goldChange} gold... Ouch...({myTime})"
        else:
            str = f"Earned {goldChange} gold from the {location}! ({myTime})"
        # Insert str to the 1st position in activities
        activities.insert(0, str)
        request.session["activities"] = activities
    return redirect("/")


def reset(request):
    # resets session data
    print("hello")
    if request.method == "POST":
        print("hello")
        request.session.flush()
        return redirect("/")
