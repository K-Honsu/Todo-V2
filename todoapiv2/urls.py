from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Todo Api",
        default_version="1.0.0",
        description="API DOCUMENTATION OF APP"
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('users/', include('users.urls')),
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('tasks/', include('tasks.urls')),
        path('docs/', schema_view.with_ui('swagger',
             cache_timeout=0), name='swagger-schema'),

    ])),
    # path('users/', include('users.urls')),
    # path('tasks/', include('tasks.urls')),
    # #
    # path('users/', include('users.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),

]
