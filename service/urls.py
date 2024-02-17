from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# router multiple views ke handle korte parbe and prottek ta views ke se delete get update egulaw korte parbe
router = DefaultRouter() #creating router
router.register('', views.ServiceViewset) #creating antena

urlpatterns = [
    path('', include(router.urls)),
]