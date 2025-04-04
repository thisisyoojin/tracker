from django.urls import path
from tracker import views

urlpatterns = [
    path('', views.dashboard_view, name="dashboard"),
]
