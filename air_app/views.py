from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = 'home.html'
# Create your views here.
