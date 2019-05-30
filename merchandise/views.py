from django.shortcuts import render
from .models import Merchandise

# Create your views here.

def all_merch(request):
    merch = Merchandise.objects.all()
    return render(request, 'merchandise.html', {'merch': merch})