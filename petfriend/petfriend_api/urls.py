#from django.conf.urls import url
from django.urls import path, include
from .views import PetView, PetDetailView, PetCreateAPIView, PetDeleteAPIView, PetUpdateAPIView

urlpatterns = [
    path('', PetView.as_view()),
    path('pet_detail/<int:pet_id>/', PetDetailView.as_view()),
    path('create/', PetCreateAPIView.as_view()),
    path('pet_detail/<int:pk>/delete/', PetDeleteAPIView.as_view()),
    path('pet_detail/<int:pk>/update/', PetUpdateAPIView.as_view()),
]