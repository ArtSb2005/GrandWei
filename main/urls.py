from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("kn", KnRostPageView.as_view(), name="kn"),
    path('kn/<int:id>/', views.KnRostPageView.detail_view, name='post_kn'),
]
