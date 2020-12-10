from django.shortcuts import render, HttpResponse
from .models import Destination
from django.contrib.auth.decorators import login_required
#import for restAPI framework 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'A City Thats Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hydrabad'
    dest2.desc = 'Love for Biryani'
    dest2.price = 500
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'IT Park'
    dest3.price = 800
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1,dest2,dest3]
    # dests = Destination.objects.all()

    return render(request, 'index.html', { 'dests': dests })

#@login_required 
def destinations(request):
    if not request.user.is_authenticated:
        #return render(request, 'index.html')
        return render(request, 'myapp/login_error.html')
    return render(request, 'destinations.html')

#restAPI
class DestinationList(APIView):

    def get(self, request):
        Destination1 = Destination.objects.all()
        serializer = DestinationSerializer(Destination1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


