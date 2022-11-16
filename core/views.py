from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def tesla(request):
    return render(request, 'tesla.html')

def ferrari(request):
    return render(request, 'ferrari.html')

def chevrolet(request):
    return render(request, 'chevrolet.html')

def kamaro(request):
    return render(request, 'kamaro.html')

def lamborgini(request):
    return render(request, 'lamborgini.html')

def mustang(request):
    return render(request, 'mustang.html')

def wolksvagen(request):
    return render(request, 'wolksvagen.html')


