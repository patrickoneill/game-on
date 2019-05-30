from django.shortcuts import render, redirect
from .models import Challenges

# Create your views here..

def challenges(request):
    result = Challenges.objects.all()
    return render(request, "challenge.html", {'challenges': result})

def post_challenge(request):
    if request.method=="POST":
        new_challenge = Challenges()
        new_challenge.name = request.POST.get("name")
        new_challenge.save()
        return redirect(challenges)
    return render(request, "post_challenge.html")
