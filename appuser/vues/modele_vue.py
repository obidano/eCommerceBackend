import json

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])  # GET est une methode utilisée principalement pour demander au serveur des données
@permission_classes([])  # Vue accesible à n'importe qui
def recupererDonneesPubliqueAPI(requete):
    donnees = [
        {"nom": "Benzema", "club": "Madrid", "Buts": 50, "active": True},
        {"nom": "Kante", "club": "Chelsea", "Buts": 0, "active": True},
        {"nom": "Zidane", "club": "Aucun", "Buts": 250, "active": False},
    ]
    reponse_serveur = dict(msg=donnees)
    return Response(reponse_serveur)


@api_view(['GET'])
def recupererDonneesProtegeesAPI(requete):
    utilisateur = "Boketshu"
    reponse_serveur = dict(msg=f"Bienvenue dans votre page monsieur {utilisateur}")
    return Response(reponse_serveur)


@api_view(['POST'])  # POST est une methode utilisée principalement pour soumettre des données  au serveur
def soumettreDonneesAPI(requete):
    # si les données sont envoyées en json, utilisez ceci  data = json.loads(reqyete.body)
    data = requete.POST.dict()  # données envoyés par le client (navigateur)
    reponse_serveur = dict(msg=f"Nous avons bien reçu vos informations", donnees=data)
    return Response(reponse_serveur)


@api_view(['PUT'])  # PUT est une methode utilisée principalement pour effectuer une mise à jour
def mettreAJourDonneesAPI(requete):
    data = requete.POST.dict()  # données envoyés par le client (navigateur)
    reponse_serveur = dict(msg=f"Vos données ont été mises à jour", donnees=data)
    return Response(reponse_serveur)
