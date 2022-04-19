from django.shortcuts import render

# Create your views here.

def cu_call(request):
    return render(request, 'Main/cu_call.html')

def co_call(request):
    return render(request, 'Main/co_call.html')

def cu_main(request):
    return render(request, 'Main/cu_main.html')

def co_main(request):
    return render(request, 'Main/co_main.html')

def star(request, star):
    return render(request, 'Main/star.html', {'star' : star})

def index(request):
    return render(request, 'Main/index.html')
