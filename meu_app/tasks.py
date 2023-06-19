
from .models import Proposta
from meu_projeto.celery import app
from celery import shared_task


@shared_task
def avaliar_proposta(proposta_id):
    proposta = Proposta.objects.get(id=proposta_id)

    if proposta.id % 2 == 0:
        proposta.status = 'Aprovado'
    else:
        proposta.status = 'Reprovado'
        
    proposta.save()

    return proposta.status

