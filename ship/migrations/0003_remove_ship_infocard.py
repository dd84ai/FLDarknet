# Generated by Django 3.1.7 on 2021-03-23 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0002_auto_20210323_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship',
            name='infocard',
        ),
    ]