from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
from .models import Place, Queue
from math import sin, cos, sqrt, atan2, radians, inf
import json, requests


class HomeView(TemplateView):
    template_name = 'vue_test.html'

    def post(self, request, *args, **kwargs):

        # json request
        json_request = json.loads(request.body)

        # user location
        x = json_request['x']
        y = json_request['y']

        #json_response = {'result': json_request['x'] + json_request['y']}
        #To też było tylko "testowe"^^^^^^^^

        json_response = {}

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


    def update_database(self, request, queues):

        for queue in queues:
            queue = Queue(
                place=queues[0],
                date=queues[1],
                time=queues[2],
                name=queues[3],
                service_time=queues[4],
                queue_lenght=queues[5],
                current_queue_number=queues[6]
            )
            queue.save()


class VueView(TemplateView):
    template_name = 'vue_full.html'
# Create your views here.

class QueueView(View):
    def get(self, request, *args, **kwargs):
        place = Place.objects.get(pk=int(self.kwargs['pk']))
        out_queues = self.get_api(place)
        return JsonResponse(out_queues, status=200)


    def get_api(self, place):

        apis = []
        queues = []

        if place == "all":  # return information about all places
            places = Place.objects.all() #Wont happen
        else:  # return information only about selected
            places = [place]

        params = ['nazwaGrupy', 'czasObslugi', 'liczbaKlwKolejce', 'aktualnyNumer']

        # everywhere the same date and time for queue
        response = requests.get(place.api)
        response_json = response.json()
        date = response_json['result']['date']
        time = response_json['result']['time']

        for place in places:
            response = requests.get(place.api)
            response_json = response.json()
            for i in range(len(response_json['result']['grupy']) - 1):
                tmp_queue = [place, date, time]
                for param in params:
                    queue = response_json['result']['grupy'][i][param]
                    tmp_queue.append(queue)
                queues.append(tmp_queue)

        return queues
