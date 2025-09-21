"""
URL configuration for rifando project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/register/', app_views.register, name='register'),
    path('dashboard/', app_views.dashboard_main, name='dashboard_main'),
    path('forgot-password/', app_views.forgot_password, name='forgot_password'),
    path('reset-password/', app_views.reset_password, name='reset_password'),
    path('dashboard/rifas/', app_views.raffle_list_admin, name='raffle_list_admin'),
    path('dashboard/rifas/create/', app_views.raffle_create, name='raffle_create'),
    path('dashboard/rifas/edit/<uuid:pk>/', app_views.raffle_edit, name='raffle_edit'),
    path('dashboard/rifas/<uuid:pk>/detail/', app_views.raffle_detail, name='raffle_detail'),
    path('dashboard/rifas/delete/<uuid:pk>/', app_views.raffle_delete, name='raffle_delete'),
    path('rifas/', app_views.raffle_list_public, name='raffle_list_public'),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
