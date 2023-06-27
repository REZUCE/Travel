from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Django проверяет url-адреса сверху вниз,
    # нам нужно, чтобы Django сначала проверял адреса в приложении users
    path('auth/', include('users.urls', namespace='users')),
    # Если какой-то URL не обнаружится в приложении users —
    # Django пойдёт искать его в django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('order/', include('orders.urls', namespace='orders')),
    path('', include('tickets.urls', namespace='tickets')),
    # path("__debug__/", include("debug_toolbar.urls")),


]
