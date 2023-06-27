from django.shortcuts import render, redirect
from .forms import TicketsSearch
from .models import Direction, Timesheet, Buses
from datetime import datetime


def ticket_search(request):
    form = TicketsSearch()
    if request.method == 'POST':
        form = TicketsSearch(request.POST)
        if form.is_valid():
            return redirect('tickets:results', send_point=form.cleaned_data['send_point'].pk,
                            points_arrival=form.cleaned_data['points_arrival'].pk,
                            date_time_departure=form.cleaned_data['date_time_departure'])
        else:
            form = TicketsSearch()
    template = 'tickets/index_search.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def ticket_search_results(request, send_point, points_arrival, date_time_departure):
    send_point = send_point
    points_arrival = points_arrival
    date_time_departure = date_time_departure[:-6]
    date_time_obj = datetime.strptime(date_time_departure, '%Y-%m-%d %H:%M:%S')
    date_time_departure = date_time_obj.date()
    try:
        directions = Direction.objects.get(
            send_point=send_point,
            points_arrival=points_arrival
        ).pk
    except Direction.DoesNotExist:
        # В случае, если не найдена запись Direction,
        # перенаправляем пользователя на другую страницу
        return render(request, 'tickets/ticket_search_results.html')

    tickets = Timesheet.objects.filter(
        direction=directions,
        date_time_departure__date=date_time_departure,
        timesheet_activity=1
    )

    now = datetime.now()
    context = {
        'tickets': tickets,
        'now': now,
    }
    return render(request, 'tickets/ticket_search_results.html', context)
