from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BusMark(models.Model):
    """Модель марка автобуса."""

    id_bus_mark = models.AutoField(db_column='id_Bus_Mark', primary_key=True)
    name_bus_mark = models.CharField(db_column='Name_Bus_Mark', max_length=25, unique=True)
    bus_mark_activity = models.BooleanField(db_column='Bus_Mark_Activity')

    def __str__(self):
        return self.name_bus_mark

    class Meta:
        managed = False
        db_table = 'bus_mark'


class BusModels(models.Model):
    """Модель автобус."""

    id_bus_models = models.AutoField(db_column='id_Bus_Models', primary_key=True)
    bus_mark = models.ForeignKey(BusMark, on_delete=models.SET_DEFAULT, db_column='Bus_Mark_id', default=2)
    name_bus_models = models.CharField(db_column='Name_Bus_Models', max_length=30)
    bus_models_activity = models.BooleanField(db_column='Bus_Models_Activity')

    class Meta:
        managed = False
        db_table = 'bus_models'


class Town(models.Model):
    """Модель город."""

    id_town = models.AutoField(db_column='id_Town', primary_key=True)
    town_name = models.CharField(db_column='Town_Name', max_length=25, unique=True)
    town_activity = models.BooleanField(db_column='Town_Activity')
    town_title = models.CharField(db_column='Town_Title', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'town'

    def __str__(self):
        return self.town_name


class BusStations(models.Model):
    """Модель автобусная станция."""

    id_bus_stations = models.AutoField(db_column='id_Bus_Stations', primary_key=True)
    town = models.OneToOneField(Town, on_delete=models.SET_DEFAULT, db_column='Town_id', default=1, unique=True)
    adress = models.CharField(db_column='Adress', max_length=100)
    bus_stations_activity = models.BooleanField(db_column='Bus_Stations_Activity')

    class Meta:
        managed = False
        db_table = 'bus_stations'


class Buses(models.Model):
    """Модель автобус."""

    id_bus = models.AutoField(db_column='id_Bus', primary_key=True)
    bus_models = models.ForeignKey(BusModels, on_delete=models.SET_DEFAULT,
                                   db_column='Bus_Models_id', default=1)
    places = models.IntegerField(db_column='Places')
    state_number = models.CharField(db_column='State_Number', max_length=10, unique=True)
    image = models.ImageField(db_column='Image', upload_to='tickets/', blank=True, null=True)
    description = models.TextField(db_column='Descripton', max_length=250, blank=True, null=True)
    bus_activity = models.BooleanField(db_column='Bus_Activity')

    class Meta:
        managed = False
        db_table = 'buses'


class Direction(models.Model):
    """Модель маршрута."""

    id_direction = models.AutoField(db_column='id_Direction', primary_key=True)
    cost_route = models.DecimalField(db_column='Cost_Route', max_digits=7, decimal_places=2)
    send_point = models.ForeignKey(
        BusStations, on_delete=models.SET_DEFAULT,
        db_column='Send_Point_id', default=1
    )
    points_arrival = models.ForeignKey(
        BusStations, on_delete=models.SET_DEFAULT,
        db_column='Points_Arrival_id',
        related_name='direction_points_arrival_set',
        default=1
    )
    direction_activity = models.BooleanField(db_column='Direction_Activity')

    class Meta:
        managed = False
        db_table = 'direction'


class TicketType(models.Model):
    """Модель тип билета."""

    id_ticket_type = models.AutoField(db_column='id_Ticket_Type', primary_key=True)
    type_name = models.CharField(db_column='Type_Name', max_length=15, unique=True)
    discount = models.DecimalField(db_column='Discount', max_digits=3, decimal_places=2)
    ticket_type_activity = models.BooleanField(db_column='Ticket_Type_Activity')

    class Meta:
        managed = False
        db_table = 'ticket_type'

    def __str__(self):
        return self.type_name


class Timesheet(models.Model):
    """Модель время отбытия/прибытия."""

    id_timesheet = models.AutoField(
        db_column='id_Timesheet', primary_key=True
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, db_column='User_id', default=1
    )
    direction = models.ForeignKey(
        Direction, on_delete=models.SET_DEFAULT, db_column='Direction_id', default=1
    )
    date_time_departure = models.DateTimeField(db_column='Date_Time_Departure')
    date_time_arrival = models.DateTimeField(db_column='Date_Time_Arrival')
    bus = models.ForeignKey(
        Buses, on_delete=models.SET_DEFAULT, db_column='Bus_id', default=1
    )
    timesheet_activity = models.BooleanField(db_column='Timesheet_Activity')
    free_place = models.IntegerField(db_column='Free_Place')

    class Meta:
        managed = False
        db_table = 'timesheet'

    def __str__(self):
        return f"{self.user} - {self.bus} ({self.date_time_departure})"
