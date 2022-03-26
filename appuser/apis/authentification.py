from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from appuser.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
# @authentication_classes([])
def connexionAPI(requete):
    a = User.objects.first()
    refresh = RefreshToken.for_user(a)

    token = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    reponse_serveur = dict(msg="Je suis connecté", u=token)
    return Response(reponse_serveur)
