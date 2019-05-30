from django.shortcuts import render
from merchandise.models import Merchandise
# Create your views here.

def do_search(request):
    merchandise = Merchandise.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'merchandise.html', {'merchandise': merchandise})