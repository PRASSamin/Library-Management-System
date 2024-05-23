# Generated by Django 5.0.6 on 2024-05-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_bookborrow_requested_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookborrow',
            name='accepted_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookborrow',
            name='borrowed_for',
            field=models.CharField(choices=[('5', '5'), ('7', '7'), ('10', '10'), ('15', '15'), ('20', '20'), ('30', '30')], default='5', max_length=2),
        ),
    ]