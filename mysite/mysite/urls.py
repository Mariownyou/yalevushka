from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cars/', include('cars.urls')),
    path('admin/', admin.site.urls),
]
