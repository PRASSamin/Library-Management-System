# Generated by Django 5.0.6 on 2024-05-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_notificationgroup_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationgroup',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
