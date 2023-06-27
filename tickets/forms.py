from django import forms
from .models import Town, Timesheet
from django_select2.forms import Select2Widget


class TicketsSearch(forms.Form):
    send_point = forms.ModelChoiceField(
        queryset=Town.objects.filter(town_activity=1),
        empty_label="Откуда",
        widget=Select2Widget()
    )
    points_arrival = forms.ModelChoiceField(
        empty_label="Куда",
        queryset=Town.objects.filter(town_activity=1),
    )

    date_time_departure = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date', 'min': '2023-01-01',
                                                                            'max': '2024-01-01'}),
                                              input_formats=['%Y-%m-%d'])

