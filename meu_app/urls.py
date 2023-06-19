from django.urls import path
from .views import PropostaCreateView

urlpatterns = [
    path('propostas/', PropostaCreateView.as_view())
]
