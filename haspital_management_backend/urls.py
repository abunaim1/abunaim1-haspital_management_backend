from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contact.urls')),
    path('services/', include('service.urls')),
    path('patients/', include('patient.urls')),
    path('doctors/', include('doctor.urls')),
    path('appointment/', include('appointment.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
