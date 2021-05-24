from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
from .models import Place
import json

class HomeView(TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
         json_request = json.loads(request.body)
         #WSTAWIAM JAKO PRZYKLAD OBLICZEN - zwrotka sumy X+Y
         json_response = {'result': json_request['x'] + json_request['y']}
         return JsonResponse(json_response, status=200)

class VueView(TemplateView):
    template_name = 'vue_test.html'
# Create your views here.
