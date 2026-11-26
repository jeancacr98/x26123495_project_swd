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
    # Protected Passenger CRUD Routes
    path('', views.dashboard, name='dashboard'), #list
    path('passenger/new/', views.passenger_create, name='passenger_create'), #form
    path('passenger/<int:pk>/edit/', views.passenger_update, name='passenger_update'), #form
    path('passenger/<int:pk>/delete/', views.passenger_delete, name='passenger_delete'), #form

]