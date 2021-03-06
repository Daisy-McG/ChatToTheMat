"""chat_to_the_mat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('chat_rooms/', include('chat_rooms.urls')),
    path('contact/', include('contact.urls')),
    path('profiles/', include('profiles.urls')),
    path('checkout/', include('checkout.urls')),
    path('private_messages/', include('private_messages.urls')),
    path('admin_panel/', include('admin_panel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
