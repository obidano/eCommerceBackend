from django.urls import path

from appuser.apis.authentification import connexionAPI, donneeConfidentielleAPI

urlpatterns = [
    # path('authentifier', connexionAPI),
    # path('confidentiel', donneeConfidentielleAPI),
]
