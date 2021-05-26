from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', csrf_exempt(views.HomeView.as_view()), name = 'home'),
    path('vue_test/', csrf_exempt(views.VueView.as_view()), name='vue_test'),
    path('<int:pk>/', views.QueueView.as_view(), name='queue'),
    path('mock/', views.MockView.as_view(), name='mock'),

]