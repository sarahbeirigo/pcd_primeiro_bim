from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from app import views as app_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
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
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
