from django.urls import path
from .views import home, appointment

urlpatterns = [
    path('', home , name='home' ),
    path('/appointment', appointment, name='appointment')
]
