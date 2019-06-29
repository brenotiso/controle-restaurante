from django.contrib import admin
from django.urls import (
    path,
    include
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('users.urls')),
]
