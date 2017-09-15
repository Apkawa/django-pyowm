# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COIndex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_time', models.DateTimeField(help_text=b'Reference time', verbose_name=b'Time the observation refers to')),
                ('interval', models.CharField(max_length=255, verbose_name=b'Time granularity of the observation', choices=[('minute', 'One minute'), ('hour', 'One hour'), ('day', 'One day'), ('month', 'One month'), ('year', 'One year')])),
                ('reception_time', models.DateTimeField(help_text=b'Reception time', null=True, verbose_name=b'Time the observation was received', blank=True)),
                ('co_samples', models.TextField(help_text=b'CO samples', verbose_name=b'CO samples data')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interval', models.CharField(help_text=b'Interval', max_length=255, verbose_name=b'Time granularity of the forecast', choices=[('3h', 'Three hours'), ('daily', 'Daily')])),
                ('reception_time', models.DateTimeField(help_text=b'Reception time', null=True, verbose_name=b'Time the observation was received', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name', max_length=255, null=True, verbose_name=b'Toponym of the place', blank=True)),
                ('lon', models.FloatField(help_text=b'Longitude', verbose_name=b'Longitude of the place')),
                ('lat', models.FloatField(help_text=b'Latitude', verbose_name=b'Latitude of the place')),
                ('city_id', models.IntegerField(help_text=b'City ID', null=True, verbose_name=b'City ID related to the place', blank=True)),
                ('country', models.CharField(help_text=b'Country', max_length=255, null=True, verbose_name=b'Country of the place', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reception_time', models.DateTimeField(null=True, blank=True)),
                ('location', models.ForeignKey(to='django_pyowm.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Ozone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_time', models.DateTimeField(help_text=b'Reference time', verbose_name=b'Time the observation refers to')),
                ('du_value', models.FloatField(help_text=b'DU value', verbose_name=b'Observed ozone Dobson Units')),
                ('interval', models.CharField(max_length=255, verbose_name=b'Time granularity of the observation', choices=[('minute', 'One minute'), ('hour', 'One hour'), ('day', 'One day'), ('month', 'One month'), ('year', 'One year')])),
                ('reception_time', models.DateTimeField(help_text=b'Reception time', null=True, verbose_name=b'Time the observation was received', blank=True)),
                ('location', models.ForeignKey(verbose_name=b'Location of the observation', to='django_pyowm.Location', help_text=b'Location')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name', max_length=255, null=True, verbose_name=b'Name of the meteostation', blank=True)),
                ('station_id', models.IntegerField(help_text=b'Station ID', verbose_name=b'OWM station ID')),
                ('station_type', models.IntegerField(help_text=b'Type', null=True, verbose_name=b'Meteostation type', blank=True)),
                ('station_status', models.IntegerField(help_text=b'Status', null=True, verbose_name=b'Meteostation status', blank=True)),
                ('lat', models.FloatField(help_text=b'Latitude', verbose_name=b'Latitude of the meteostation')),
                ('lon', models.FloatField(help_text=b'Longitude', verbose_name=b'Longitude of the meteostation')),
                ('distance', models.FloatField(help_text=b'Distance', null=True, verbose_name=b'Distance of station from lat/lon of search criteria', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('station_id', models.IntegerField(help_text=b'Station ID', verbose_name=b'OWM station ID')),
                ('interval', models.CharField(help_text=b'Interval', max_length=255, verbose_name=b'Time granularity of the station history', choices=[('tick', 'Tick'), ('hour', 'One hour'), ('day', 'One day')])),
                ('reception_time', models.DateTimeField(help_text=b'Reception time', null=True, verbose_name=b'Time the observation was received', blank=True)),
                ('measurements', models.TextField(help_text=b'Measurements', verbose_name=b'Measured data')),
            ],
        ),
        migrations.CreateModel(
            name='UVIndex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_time', models.DateTimeField(help_text=b'Reference time', verbose_name=b'Time the observation refers to')),
                ('value', models.FloatField(help_text=b'Value', verbose_name=b'Observed UV intensity')),
                ('interval', models.CharField(help_text=b'Interval', max_length=255, verbose_name=b'Time granularity of the observation', choices=[('minute', 'One minute'), ('hour', 'One hour'), ('day', 'One day'), ('month', 'One month'), ('year', 'One year')])),
                ('reception_time', models.DateTimeField(help_text=b'Reception time', null=True, verbose_name=b'Time the observation was received', blank=True)),
                ('location', models.ForeignKey(verbose_name=b'Location of the observation', to='django_pyowm.Location', help_text=b'Location')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_time', models.DateTimeField()),
                ('sunrise_time', models.DateTimeField(null=True, blank=True)),
                ('sunset_time', models.DateTimeField(null=True, blank=True)),
                ('clouds', models.PositiveIntegerField(null=True, blank=True)),
                ('rain', models.CharField(max_length=255, null=True, blank=True)),
                ('snow', models.CharField(max_length=255, null=True, blank=True)),
                ('wind', models.CharField(max_length=255, null=True, blank=True)),
                ('humidity', models.PositiveIntegerField(null=True, blank=True)),
                ('pressure', models.CharField(max_length=255, null=True, blank=True)),
                ('temperature', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.CharField(max_length=255)),
                ('detailed_status', models.CharField(max_length=255)),
                ('weather_code', models.IntegerField()),
                ('weather_icon_name', models.CharField(max_length=255, null=True, blank=True)),
                ('visibility_distance', models.FloatField(null=True, blank=True)),
                ('dewpoint', models.FloatField(null=True, blank=True)),
                ('humidex', models.FloatField(null=True, blank=True)),
                ('heat_index', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='last_weather',
            field=models.ForeignKey(blank=True, to='django_pyowm.Weather', help_text=b'Last weather', null=True, verbose_name=b'Last weather measured by the station'),
        ),
        migrations.AddField(
            model_name='observation',
            name='weather',
            field=models.ForeignKey(to='django_pyowm.Weather'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='location',
            field=models.ForeignKey(verbose_name=b'Location of the forecast', to='django_pyowm.Location', help_text=b'Location'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='weathers',
            field=models.ManyToManyField(help_text=b'Weathers', related_name='forecasts', verbose_name=b'Weathers of the forecast', to='django_pyowm.Weather'),
        ),
        migrations.AddField(
            model_name='coindex',
            name='location',
            field=models.ForeignKey(verbose_name=b'Location of the observation', to='django_pyowm.Location', help_text=b'Location'),
        ),
    ]
