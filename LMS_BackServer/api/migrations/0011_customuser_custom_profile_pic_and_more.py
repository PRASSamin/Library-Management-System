# Generated by Django 5.0.6 on 2024-05-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_activitylog'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='custom_profile_pic',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='cover_pic_url',
            field=models.CharField(blank=True, editable=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic_url',
            field=models.CharField(blank=True, editable=False, max_length=500, null=True),
        ),
    ]
