from django.urls import path

from . import views
from .views import ContactView

urlpatterns = [
    path('', views.index, name='index'),
    path('rubber/', views.rubber, name='rubber'),
    path('discs/', views.disc, name='disc'),
    path('contact/', ContactView.as_view(), name='contact'),
]
