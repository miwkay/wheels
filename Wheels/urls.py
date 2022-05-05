from django.contrib import admin
from django.urls import include, path

from wheels.views import DiscAPIView, RubberAPIView


urlpatterns = [
    path('', include('wheels.urls')),
    path('admin/', admin.site.urls),
    path('rubber/', include('wheels.urls')),
    path('discs/', include('wheels.urls')),
    path('api/disc/', DiscAPIView.as_view()),
    path('api/rubber/', RubberAPIView.as_view()),
]
