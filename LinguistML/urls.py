"""
URL configuration for LinguistML project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from LinguistML.views import ping
import environ


env = environ.Env()
environ.Env.read_env()

BASE_URL_PREFIX = env("BASE_URL_PREFIX", default="api/v1")



urlpatterns = [
    path(f"{BASE_URL_PREFIX}/ping", ping),
    path(f'{BASE_URL_PREFIX}/admin/', admin.site.urls, name="admin")    ,
    path(f'{BASE_URL_PREFIX}/chat/', include('chat.urls'), name="chat"),
    path(f'{BASE_URL_PREFIX}/profile/', include('profiling.urls'), name="profiling"),
]


# Custom Error Pages

handler404 = 'LinguistML.exception_handlers.custom_404_view'
handler500 = 'LinguistML.exception_handlers.custom_500_view'