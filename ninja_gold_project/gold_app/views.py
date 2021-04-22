from django.shortcuts import render, redirect
import random


def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    return render(request, "index.html")  # add context


def process_money(request):
    if request.method == "POST":
        location = request.POST["location"]
        if location == "farm":
            request.session["gold"] += random.randint(10, 20)
        elif location == "cave":
            request.session["gold"] += random.randint(5, 10)
        elif location == "house":
            request.session["gold"] += random.randint(2, 5)
        else:
            request.session["gold"] += random.randint(-50, 50)
        print(request.session["gold"])
    return redirect("/")
