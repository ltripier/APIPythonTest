from django.urls import path
from .views import ApiView, PersonnageDetailApiView
from .tests import APITestCase

urlpatterns = [
    path('api/', ApiView.as_view(), name=''),
    path('api/<int:id>/', PersonnageDetailApiView.as_view(), name='details'),
]