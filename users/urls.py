from django.urls import path
from .views import (
    token,
    refresh_token,
    revoke_token
)

urlpatterns = [
    path('token/', token),
    path('token/refresh/', refresh_token),
    path('token/revoke/', revoke_token),
]
