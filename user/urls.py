from django.urls import include, path
from rest_framework.routers import DefaultRouter
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework_simplejwt.views import TokenVerifyView

from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, 'user')

urlpatterns = [
    path("", include(router.urls)),
    path("auth/login", LoginView.as_view()),
    path("auth/logout/", LogoutView.as_view()),
    path("auth/token/verify/", TokenVerifyView.as_view()),
    path("auth/token/refresh/", get_refresh_view().as_view()),
]
