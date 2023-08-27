#from django.conf.urls import url
from django.urls import path, include
from .views import PetView

urlpatterns = [
    path('', PetView.as_view()),
]