from django.contrib import admin
from django.urls import path, include
from petfriend_proj.petfriend_proj import urls as petfriend_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(petfriend_urls)),
]