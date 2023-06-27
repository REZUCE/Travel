from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'orders'

urlpatterns = [
    path(
        '<int:timesheet_id>/',
        views.order,
        name='order'
    ),
    path('passenger/<int:id_order>/<int:id_timesheet>/', views.passenger, name='passenger'),
    path('passenger/success/', views.success, name='success'),
    path('tickets/', views.tickets, name='tickets')
]
