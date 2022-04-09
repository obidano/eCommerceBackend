"""eCommerceBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from appuser.views import liste_clients_api
from appuser.vues.authentification_vue import authentificationAPI
from appuser.vues.modele_vue import recupererDonneesPubliqueAPI, recupererDonneesProtegeesAPI, soumettreDonneesAPI, \
    mettreAJourDonneesAPI

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # """INSERER VOS LIENS ICI """
                  # path('client/liste', liste_clients_api),
                  path('api/public_data', recupererDonneesPubliqueAPI),
                  # path('api/private_data', recupererDonneesProtegeesAPI),
                  # path('api/soumettre_data', soumettreDonneesAPI),
                  # path('api/update_data', mettreAJourDonneesAPI),

                  # path('api/user/authentifier', authentificationAPI),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
