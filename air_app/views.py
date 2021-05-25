from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
from .models import Place
from math import sin, cos, sqrt, atan2, radians, inf
import json


class HomeView(TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):

        # json request
        json_request = json.loads(request.body)

        # user location
        x = json_request['x']
        y = json_request['y']

        #json_response = {'result': json_request['x'] + json_request['y']}
        #To też było tylko "testowe"^^^^^^^^
        places = Place.objects.all()
        closest_place_distance = inf
        closest_place = ""

        for place in places:
            current_place_distance = self.calculate_distance(x, y, place.x, place.y, place.name)[0]
            if current_place_distance < closest_place_distance:
                closest_place_distance = current_place_distance
                closest_place = self.calculate_distance(x, y, place.x, place.y, place.name)[1]

        json_response['place_name'] = closest_place
        json_response['distance'] = closest_place_distance


        # JAKO DALSZY PRZYKŁAD - wyciągam pierwszy obiekt Place, dodaje jego nazwe do response
        # place = Place.objects.all()[0]
        # json_response['place_name'] = place.name
        # json_response['distance'] = place.x + place.y  # ogarnac jak sie oblicza odleglosc z wspolrzednych

        return JsonResponse(json_response, status=200)

    def calculate_distance(self, x_user, y_user, x_office, y_office, office_name):
        # approximate radius of earth in km
        r = 6373.0

        # latitude = x, longitude = y
        lat1 = radians(x_user)
        lon1 = radians(y_user)
        lat2 = radians(x_office)
        lon2 = radians(y_office)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = r * c

        return distance, office_name


class VueView(TemplateView):
    template_name = 'vue_test.html'
# Create your views here.
