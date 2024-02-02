# Generated by Django 4.2.6 on 2024-01-28 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApartmentNumber', models.IntegerField()),
                ('NumBedrooms', models.IntegerField()),
                ('NumBathrooms', models.IntegerField()),
                ('RentAmount', models.IntegerField()),
                ('LeaseStartDate', models.DateField(auto_now_add=True)),
                ('LeaseEndDate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuildingID', models.IntegerField()),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenantID', models.IntegerField()),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PropertyManagerID', models.IntegerField()),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.building')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestID', models.IntegerField()),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.apartment')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.tenant')),
            ],
        ),
    ]