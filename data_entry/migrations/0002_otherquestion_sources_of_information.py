# Generated by Django 2.0.4 on 2018-06-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherquestion',
            name='sources_of_information',
            field=models.ManyToManyField(blank=True, max_length=20, null=True, to='data_entry.SourcesOfInformation', verbose_name='which sources of         information does your organisation utilize to inform HIV programming and decision making?'),
        ),
    ]
