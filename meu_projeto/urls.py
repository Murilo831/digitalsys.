
from django.contrib import admin
from django.urls import path, include

from meu_app.views import PropostaCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('meu_app.urls')),
    
]
