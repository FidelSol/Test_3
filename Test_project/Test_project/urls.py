"""Test_project URL Configuration
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from poll.views import PersonalsViewSet, TestsViewSet, PhotosViewSet, UsersViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'api/v1/personals', PersonalsViewSet, basename='Personals')
router.register(r'api/v1/tests', TestsViewSet, basename='Tests')
router.register(r'api/v1/photos', PhotosViewSet, basename='Photos')
router.register(r'api/v1/users', UsersViewSet, basename='Users')

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="poll/registration/login.html"),
                       name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(template_name="registration/logged_out.html"),
                       name='logged_out'),
    path('password-reset/',
                       auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
                       name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
                      template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                      template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
                      template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
                      template_name="registration/password_change_form.html"), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
                      template_name="registration/password_change_done.html"), name='password_change_done'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include('poll.urls')),
] + router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
