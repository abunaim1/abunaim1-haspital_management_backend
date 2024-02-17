from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter() #wifi router create
router.register('', views.AppointmentViewset) # and their antena create

urlpatterns = [
     path('', include(router.urls)),
]
