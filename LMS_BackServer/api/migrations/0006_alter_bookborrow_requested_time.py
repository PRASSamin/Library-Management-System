# Generated by Django 5.0.6 on 2024-05-10 12:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_bookborrow_late_fine_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookborrow',
            name='requested_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]