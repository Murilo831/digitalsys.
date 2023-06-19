from rest_framework import generics
from .models import Proposta
from .serializers import PropostaSerializer

from .tasks import avaliar_proposta


class PropostaCreateView(generics.CreateAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def perform_create(self, serializer):
        proposta = serializer.save()

        avaliar_proposta.delay(proposta.id)
