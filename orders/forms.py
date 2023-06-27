from datetime import datetime
from random import randint

from django import forms
from .models import Order
from tickets.models import Timesheet, TicketType
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderForm(forms.ModelForm):
    number_tickets = forms.IntegerField(
        label='Количество билетов',
        min_value=1,
        max_value=3,
        initial=1,  # значение по умолчанию
        required=False,
        widget=forms.HiddenInput(),
    )
    ticket_type = forms.ModelChoiceField(
        label='Выберите тариф',
        queryset=TicketType.objects.all()
    )

    class Meta:
        model = Order
        fields = ['ticket_type', 'number_tickets']

        widgets = {
            'user': forms.HiddenInput(),
            'data_order': forms.HiddenInput(),
            'timesheet': forms.HiddenInput(),

        }


class PassengerForm(forms.Form):
    name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    patronymic = forms.CharField(label='Отчество', required=False)
    birth_date = forms.CharField(label='Дата рождения')  # widget=forms.TextInput(attrs={'mask': '11.11.1111'})
    gender = forms.ChoiceField(label='Пол', choices=[('М', 'Мужской'), ('Ж', 'Женский')])
    document_type = forms.ChoiceField(label='Тип документа', choices=[('passport', 'Паспорт'), (
        'birth_certificate', 'Свидетельство о рождении')])
    document_number = forms.CharField(label='Номер документа')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document_type'].widget.attrs['onchange'] = 'updateMaxLength()'

    # class Media:
    #     js = ('passenger_form.js', )
