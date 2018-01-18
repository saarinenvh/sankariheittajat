from django.shortcuts import render
from .models import uutiset
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    uutinen = uutiset.objects.all()
    return render(request, 'index.html', context = {'uutiset': uutinen})

def jasenyys(request):
    return render(request, 'jasenyys.html')

def kalenteri(request):
    return render(request, 'kalenteri.html')

def keskustelu(request):
    return render(request, 'keskustelu.html')

def saannot(request):
    return render(request, 'saannot.html')

def seura(request):
    return render(request, 'seura.html')
