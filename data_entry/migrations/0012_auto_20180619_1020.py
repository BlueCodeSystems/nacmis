# Generated by Django 2.0.5 on 2018-06-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0011_auto_20180619_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stakeholderdirectory',
            options={'verbose_name_plural': 'Stakeholder directory'},
        ),
        migrations.AlterField(
            model_name='stakeholderdirectory',
            name='gps',
            field=models.CharField(blank=True, help_text='use decimal degrees format(ie: -15.38753, 28.32282)', max_length=20, verbose_name='GPS Coordinates'),
        ),
    ]