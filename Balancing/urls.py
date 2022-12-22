from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("balancing", BalancingPageView.as_view(), name="balancing"),
    path('/<int:id>/', views.BalancingPageView.detail_view, name='post_balancing'),
]