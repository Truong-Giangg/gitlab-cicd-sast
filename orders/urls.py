from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
