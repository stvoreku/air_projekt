from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
from .models import Place, Queue
from math import sin, cos, sqrt, atan2, radians, inf
import json, requests, numpy


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
        return JsonResponse({'queues': out_queues}, status=200)


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


class MockView(View):

    def get(self, request, *args, **kwargs):
        place = pk=int(self.kwargs['pk'])
        self.update_mock_database(self.get_api(placeid=place))
        return JsonResponse({'queues': "dsadsad"}, status=200)

    def mock_queue(self):

        probe = []

        y = 0

        for i in range(0, 33):
            if i in range(0, 4):  # 8
                x = numpy.random.randint(0, 5)
                probe.append(x)
            elif i in range(5, 9):  # 9
                y = probe[3]
                probe.append(y + numpy.random.randint(1, 3))
            elif i in range(9, 13):  # 10
                y = probe[7]
                probe.append(y - numpy.random.randint(0, 3))
            elif i in range(13, 17):  # 11
                y = probe[11]
                probe.append(y - numpy.random.randint(1, 3))
            elif i in range(17, 21):  # 12
                y = probe[15]
                probe.append(y + numpy.random.randint(1, 4))
            elif i in range(21, 23):  # 13
                y = probe[19]
                probe.append(y + numpy.random.randint(3, 6))
            elif i in range(23, 25):  # 13:30
                y = probe[21]
                probe.append(y - numpy.random.randint(1, 2))
            elif i in range(25, 29):  # 14
                y = probe[23]
                probe.append(y - numpy.random.randint(1, 6))
            elif i in range(29, 31):  # 15
                y = probe[27]
                probe.append(y + numpy.random.randint(2, 4))
            elif i in range(31, 33):  # 15:30
                y = probe[29]
                probe.append(y - numpy.random.randint(1, 4))

            if probe[i - 1] < 0:  # check if queue < 0
                probe[i - 1] = 0

        return probe

    def get_api(self, placeid):

        places = [Place.objects.get(id=placeid)]
        params = ['nazwaGrupy', 'czasObslugi', 'aktualnyNumer']
        queues = []
        j = 0

        times = ["8:00", "8:15", "8:30", "8:45",
                 "9:00", "9:15", "9:30", "9:45",
                 "10:00", "10:15", "10:30", "10:45",
                 "11:00", "11:15", "11:30", "11:45",
                 "12:00", "12:15", "12:30", "12:45",
                 "13:00", "13:15", "13:30", "13:45",
                 "14:00", "14:15", "14:30", "14:45",
                 "15:00", "15:15", "15:30", "15:45"]

        mock_queues = []

        for x in range(0, 100):
            mock_queue = self.mock_queue()
            mock_queues.append(mock_queue)


        for time in times:
            for place in places:
                response = requests.get(place.api)
                response_json = response.json()
                for i in range(len(response_json['result']['grupy']) - 1):
                    tmp_queue = [place, 4, time]  # 4 for thursday
                    for param in params:
                        x = response_json['result']['grupy'][i][param]
                        tmp_queue.append(x)
                    tmp_queue.append(mock_queues[i][j])
                    queues.append(tmp_queue)
            j += 1

        return queues

    def update_mock_database(self, queues):
        for queue in queues:
            queue = Queue(
                place=queues[0],
                num_of_week=queues[1],
                time=queues[2],
                name=queues[3],
                service_time=queues[4],
                queue_lenght=queues[6],
                current_queue_number=queues[5]
            )
            queue.save()




