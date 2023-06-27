from django.db import models
from tickets.models import TicketType, Timesheet
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    id_order = models.AutoField(db_column='id_Order', primary_key=True)
    timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE, db_column='Timesheet_id')
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, db_column='Ticket_Type_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='User_id')
    data_order = models.DateTimeField(db_column='Data_Order')
    number_tickets = models.IntegerField(db_column='Number_Tickets')
    cost_total = models.DecimalField(db_column='Cost_Total', max_digits=10, decimal_places=2)
    order_status = models.BooleanField(db_column='Order_Status')

    class Meta:
        managed = False
        db_table = 'order'
