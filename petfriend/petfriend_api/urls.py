from django.contrib import admin
from django.urls import path, include
from petfriend_proj.petfriend_proj import urls as petfriend_urls
from serializers import PetSerializer, FullPetSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('pet_api/', include(petfriend_urls)),
]