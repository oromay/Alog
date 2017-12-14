import datetime

from django.shortcuts import render
from .models import New, Post

now = datetime.datetime.now()




def mainpage(request):
    context = {
        'news': New.objects.all(),
        'posts' : Post.objects.all(),
        'title': "Голоса Африки",
        'year' : now.year,
    }
    return render(request, "home.html", context)
