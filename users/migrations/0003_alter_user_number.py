# Generated by Django 4.2.1 on 2023-06-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, db_column='Number', max_length=15, null=True, verbose_name='Номер телефона'),
        ),
    ]
