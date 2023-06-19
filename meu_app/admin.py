from django.contrib import admin
from .models import Proposta

class PropostaAdmin(admin.ModelAdmin):
    list_display=('nome', 'cpf', 'status')

admin.site.register(Proposta, PropostaAdmin)

