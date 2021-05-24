from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
from .models import Place

class HomeView(TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
         return JsonResponse({'id': request.POST.get('x')}, status=200)

class VueView(TemplateView):
    template_name = 'vue_test.html'
# Create your views here.
