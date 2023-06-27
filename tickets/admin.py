from django.contrib import admin
from .models import BusMark, Buses, BusModels, BusStations
from .models import Town, Timesheet, TicketType, Direction

admin.site.register(BusMark)
admin.site.register(Buses)
admin.site.register(BusModels)
admin.site.register(BusStations)
admin.site.register(Town)
admin.site.register(Timesheet)
admin.site.register(TicketType)
admin.site.register(Direction)
