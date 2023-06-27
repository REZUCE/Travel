from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.core.mail import send_mail
from .forms import OrderForm, PassengerForm
from tickets.models import Timesheet
from django.contrib.auth import get_user_model
from datetime import datetime
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required
def order(request, timesheet_id):
    template = 'orders/order.html'
    timesheet = get_object_or_404(Timesheet, id_timesheet=timesheet_id)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order_ = form.save(commit=False)
        order_.user = request.user
        order_.data_order = datetime.now()
        order_.timesheet = timesheet
        order_.cost_total = 0
        order_.order_status = 0
        order_.save()
        return redirect('orders:passenger', id_timesheet=timesheet.pk, id_order=order_.pk)
    else:
        render(request, 'orders/order.html')
    return render(request, template, {'form': form})


@login_required
def passenger(request, id_order, id_timesheet):
    timesheet = get_object_or_404(Timesheet, id_timesheet=id_timesheet)
    order_ = get_object_or_404(Order, id_order=id_order)
    ticket_type = order_.ticket_type.discount
    direction = timesheet.direction.cost_route
    order_.cost_total = direction * ticket_type
    order_.save()
    form = PassengerForm(request.POST or None)
    if form.is_valid():
        timesheet.free_place = timesheet.free_place - 1
        timesheet.save()
        order_.order_status = 1
        order_.save()
        email = request.user.mail
        bus_state_number = timesheet.bus.state_number
        send_point = timesheet.direction.send_point
        points_arrival = timesheet.direction.points_arrival
        cost_total = order_.cost_total
        date_departure = timesheet.date_time_departure
        date_arrival = timesheet.date_time_arrival
        driver_name = timesheet.user.name
        driver_lastname = timesheet.user.lastname

        bus_mark = timesheet.bus.bus_models.bus_mark.name_bus_mark
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        patronymic = form.cleaned_data['patronymic']
        birth_date = form.cleaned_data['birth_date']
        gender = form.cleaned_data['gender']
        document_number = form.cleaned_data['document_number']
        ticket_type = order_.ticket_type.type_name
        html = render_to_string('orders/email_buy.html', {
            'email': email,
            'bus_state_number': bus_state_number,
            'send_point': send_point,
            'cost_total': cost_total,
            'date_arrival': date_arrival,
            'date_departure': date_departure,
            'name': name,
            'bus_mark': bus_mark,
            'driver_name': driver_name,
            'driver_lastname': driver_lastname,
            'document_number': document_number,
            'gender': gender,
            'birth_date': birth_date,
            'last_name': last_name,
            'patronymic': patronymic,
            'ticket_type': ticket_type,
            'points_arrival': points_arrival
        })
        send_mail(
            f'Star Bus: Уважаемый клиент, {order_.user.lastname} {order_.user.name} {order_.user.patronymic}. Ваш билет оформлен!',
            'Благодарим вас.',
            'noreplystarbus@gmail.com',
            [email, ],
            fail_silently=False,
            html_message=html,
        )
        return redirect('orders:success')

    template = 'orders/passenger.html'
    return render(request, template, context={
        'form': form,
        'order_cost_total': order_.cost_total
    })


@login_required()
def success(request):
    return render(request, 'orders/success.html')


def tickets(request):
    return render(request, 'orders/email_buy.html')
