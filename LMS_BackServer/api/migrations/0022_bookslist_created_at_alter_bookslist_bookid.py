# Generated by Django 5.0.6 on 2024-05-21 14:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_bookslist_label_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookslist',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='bookslist',
            name='bookID',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
    ]
