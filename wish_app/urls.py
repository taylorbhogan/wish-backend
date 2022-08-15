from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlists', views.find_wishlists, name="find_wishlists")
]
