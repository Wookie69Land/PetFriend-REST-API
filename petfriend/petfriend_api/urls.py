#from django.conf.urls import url
from django.urls import path, include
from .views import PetView, PetDetailView

urlpatterns = [
    path('', PetView.as_view()),
    path('pet_detail/', PetDetailView.as_view())
]