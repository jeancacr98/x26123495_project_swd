from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Enable login, logout and reset password
    path('', include('django.contrib.auth.urls')),
]