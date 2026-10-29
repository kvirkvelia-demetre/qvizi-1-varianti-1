from django.shortcuts import render

def product(request):
    produqtebi = {
        'Laptop' : "2500 GEl",
        'Mouse' : '80 GEL',
        'Keyboard' : '150 GEL',
        'Monitor' : '700 GEL'
    }
    return render(request, 'product.html', produqtebi)

def home(request):
