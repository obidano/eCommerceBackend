from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def connexionAPI(requete):
    reponse_serveur = dict(msg="Je suis connecté")
    return Response(reponse_serveur)
