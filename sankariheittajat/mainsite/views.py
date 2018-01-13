from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

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

def uutiset(request):
    return render(request, 'uutiset.html')
