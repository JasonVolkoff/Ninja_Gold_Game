from django.shortcuts import render, redirect


def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0

    return render(request, "index.html")


def process_money(request):
    # check if info is posted
    if request.method == "POST":
        # convert to simple variables to ease of use
        totalGold = request.session["gold"]
        location = request.session["location"]
        # check where we're at
        if location == "farm":
            # Earns 10-20g
            goldThisTurn = round(random.random() * 10 + 10)
            # add total with session gold
            totalGold += goldThisTurn
            request.session["gold"] = totalGold
    return redirect("/")
