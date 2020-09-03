"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic.base import RedirectView
from apps.characters.views import GetProfileInformation
from apps.awards.views import LoginWithToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/personaje/")),
    path("personaje/", include("apps.characters.urls")),
    path("logros/", include("apps.achievements.urls")),
    path("awards/", include("apps.awards.urls")),
    path("negocio/", include("apps.business.urls")),
    path("obtener-datos/", view=GetProfileInformation.as_view(), name="getData"),
    path(route="logout/", view=LogoutView.as_view(), name="logout"),
    path(route="login/<slug:uuid>", view=LoginWithToken.as_view(), name="login"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path(route="api/", view=include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
