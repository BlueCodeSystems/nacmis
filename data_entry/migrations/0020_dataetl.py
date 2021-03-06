# Generated by Django 2.0.4 on 2018-08-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0019_auto_20180828_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataElementName', models.CharField(max_length=160)),
                ('dataElementID', models.CharField(max_length=100)),
                ('orgUnitName', models.CharField(max_length=100)),
                ('orgUnitID', models.CharField(max_length=100)),
                ('period', models.PositiveIntegerField(max_length=10)),
                ('value', models.PositiveIntegerField()),
            ],
        ),
    ]
