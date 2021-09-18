from django.shortcuts import render

def home(request):
    context = {}
    return render(request,'app/index.html', context)


def appointment(request):
    context = {}
    return render(request,'app/appointment.html', context)