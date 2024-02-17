# serializer python er model take JSON e convert kore dibe 
# jate kore jekono jaigai amra ei API take use korte parii
# Front end er sathe back end er comunication medium tai hocche JSON


from rest_framework import serializers
from . import models

class AppointmentSerializers(serializers.ModelSerializer):
    time = serializers.StringRelatedField()
    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    class Meta:
        model = models.Appointment
        fields = "__all__"