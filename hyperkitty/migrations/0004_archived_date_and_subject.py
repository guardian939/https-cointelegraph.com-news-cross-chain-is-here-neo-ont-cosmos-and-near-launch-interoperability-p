# -*- coding: utf-8 -*-
# flake8: noqa

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyperkitty', '0003_thread_starting_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='archived_date',
            field=models.DateTimeField(default=django.utils.timezone.now, db_index=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.CharField(max_length=512, db_index=True),
        ),
    ]
