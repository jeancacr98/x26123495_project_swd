from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from flights import views

# Mandatory authentication routing 
urlpatterns = [
    #Administration Panel
    path('admin/', admin.site.urls),
    #Succesful login redirects to the dashboard
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    #Add all the urls not classified
    path('', include('django.contrib.auth.urls')),
    #Main passenger dashboard
    path('', views.dashboard, name='dashboard'),
]