from django.shortcuts import render
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes


# Create your views here.
@api_view(['GET'])
@permission_classes([])
def liste_clients_api(request):
    # gener des données aleatoires
    data = []
    liste_prenom = ['Medhi', 'Valha', 'Hugues', 'Iya', 'Michée',
                    'Dorcas', 'Mbondos', 'Gilbert', 'Gogno']
    liste_nom = ['CHirali', 'Malongo', 'Soso', "Amale", "Bolasie",
                 "Mbanzu"]
    for i in range(0, 20):
        nom = random.choice(liste_nom)
        prenom = random.choice(liste_prenom)
        age = random.randint(20, 40)

        client = dict(nom=nom, prenom=prenom, age=age)
        data.append(client)

    data2 = [
        dict(nom="A", prenom="AA", age=10),
        dict(nom="B", prenom="BB", age=30),
    ]
    return Response(dict(clients=data))
    # return Response(dict(clients=data2))
