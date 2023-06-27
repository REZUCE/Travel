from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('me/', views.AboutMeView.as_view(), name='me'),
]
