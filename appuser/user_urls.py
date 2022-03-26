from django.urls import path

from appuser.apis.authentification import connexionAPI

urlpatterns = [
    path('authentifier/', connexionAPI),
]
