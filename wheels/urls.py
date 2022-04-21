from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rubber/', views.rubber, name='rubber'),
    path('discs/', views.disc, name='disc'),
]
