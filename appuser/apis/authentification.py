from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from appuser.models import User
import json


@api_view(['POST'])
@permission_classes([])
def connexionAPI(requete):
    data = json.loads(requete.body)
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


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def donneeConfidentielleAPI(requete):
    username = requete.user.username
    reponse_serveur = dict(msg=f"Je suis autorisé à consulter ces données en tant que {username}")
    return Response(reponse_serveur)
