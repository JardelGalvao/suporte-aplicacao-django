# Generated by Django 4.2.6 on 2023-10-31 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encaminhamentos_incorretos', '0003_encaminhamento_ss_alter_encaminhamento_datahora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encaminhamento',
            name='datahora',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 17, 13, 23, 57721)),
        ),
        migrations.AlterField(
            model_name='ignorarmes',
            name='mes',
            field=models.IntegerField(),
        ),
    ]