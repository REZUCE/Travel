from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'tickets'

urlpatterns = [
    path(
        'results/<int:send_point>/<int:points_arrival>/<str:date_time_departure>/',
        views.ticket_search_results,
        name='results'
    ),
    path('', views.ticket_search, name='index_search')

]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
#     )
