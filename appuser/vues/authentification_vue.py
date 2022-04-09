import json

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
@permission_classes([])
def connexionAPI(requete):
    data = requete.POST.dict()
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    if not user:
        message_erreur = dict(msg="Echec authentification")
        return Response(message_erreur, status=500)

    login(requete, user)
    token = RefreshToken.for_user(user)

    reponse_serveur = dict(msg="Je suis connecté", token=str(token.access_token))
    return Response(reponse_serveur)



