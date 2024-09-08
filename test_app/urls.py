from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('protected', views.protected_view, name='protected')
]
