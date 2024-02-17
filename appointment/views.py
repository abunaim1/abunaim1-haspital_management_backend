from rest_framework import viewsets
from . import models
from . import serializers


class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all() 
    serializer_class = serializers.AppointmentSerializers
    # appointment model er object gula nilam then setake json e convert serializer class e diye dilam,, egulo automatically hote thakbe in built vabe 

    # custom query kortechii
    def get_queryset(self):
        queryset = super().get_queryset() # 7 no. line ke niye aslam othoba parent ke inherit korlam
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
