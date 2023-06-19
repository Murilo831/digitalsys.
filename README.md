# Sistema de Gestão de Proposta de Empréstimo Pessoal

> Status: Completo 
<p> Esse é um Sistema de Gestão de Proposta de Empréstimo Pessoal, onde utilizei <strong>React</strong> no seu frontend para o cadastro do <strong>nome, cpf, endereço e valor do empréstimo</strong> , com toda comunicação feita apartir do DJANGO REST FRAMEWORK.

Assim que a proposta é preenchida e enviada, por padrão ela vai para o Banco de Dados <strong>(POSTGRES) no Docker</strong> como reprovada, sendo enviada para uma <strong>fila RabbitMQ.</strong> 
  
Fazendo com que o <strong>Celery</strong>  seja responsável por avaliar a proposta com o status de "Reprovada" ou "Aprovada", nesse caso a lógica aplicada foi a seguinte: 
```python
# tasks.py
def avaliar_proposta(proposta_id):
    proposta = Proposta.objects.get(id=proposta_id)

    if proposta.id % 2 == 0:
        proposta.status = 'Aprovado'
    else:
        proposta.status = 'Reprovado'
        
    proposta.save()
</p>
```

## Super user: digitalsys | Senha: digitalsys96321

## Fields do Model

+ Nome
+ cpf
+ enderco
+ valor_emprestimo
+ status

## Principais tecnologias usadas

<table>
  <tr>
    <td> Python </td>
    <td> Django </td>
    <td> Celery </td>
    <td> Django Rest Framework </td>
    <td> Postgres </td>
    <td> Redis </td>
  </tr>
  <tr>
    <td> 3.10.6 </td>
    <td> 4.2.2 </td>
    <td> 5.3.0 </td>
    <td> 3.14.0 </td>
    <td> 2.9.6 </td>
    <td> 4.5.5 </td>
  </tr>
</table>

## Como rodar a aplicação

+ sudo docker-compose up
+ npm start
+ python manage.py runserver 8080
+ celery -A meu_projeto worker --loglevel=info
