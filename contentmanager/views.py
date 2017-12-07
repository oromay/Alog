from django.shortcuts import render
import datetime

now = datetime.datetime.now()

def mainpage(request):
    context = {
        'title': "Голоса Африки",
        'year' : now.year
    }
    return render(request, "home.html", context)
