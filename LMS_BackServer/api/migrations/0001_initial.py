# Generated by Django 5.0.6 on 2024-05-09 17:32

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('borrow_id', models.CharField(default='veK0bKWE7xNMc9c', max_length=100, unique=True)),
                ('bookID', models.CharField(max_length=100)),
                ('borrowed_for', models.CharField(choices=[('1', '1'), ('5', '5'), ('7', '7'), ('10', '10'), ('15', '15'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('20', '20'), ('30', '30')], default='5', max_length=2)),
                ('requested_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('borrowed', 'borrowed'), ('Overdue', 'Overdue'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], default='Pending', max_length=100)),
                ('message', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=100)),
                ('userUID', models.CharField(max_length=100, unique=True)),
                ('userdp', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('timeUp', models.BooleanField(default=False)),
                ('isReturned', models.BooleanField(default=False)),
                ('isEmailSend', models.BooleanField(default=False)),
                ('request_handled_by', models.CharField(blank=True, max_length=100, null=True)),
                ('late_fine', models.IntegerField(blank=True, default=0, null=True)),
                ('remaining_days', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='booksList',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bookID', models.CharField(blank=True, max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=150)),
                ('publish_date', models.DateField()),
                ('pages', models.IntegerField()),
                ('available', models.BooleanField()),
                ('thumbnail', models.CharField(max_length=150)),
                ('language', models.CharField(max_length=150)),
                ('book_available', models.IntegerField(default=0)),
                ('genre', models.CharField(max_length=150)),
                ('ISBN', models.CharField(max_length=150)),
                ('website', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CSRFToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('csrf_token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('expired_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='libraryImage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('expired_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('profile_pic_url', models.CharField(blank=True, max_length=500, null=True)),
                ('cover_pic', models.ImageField(blank=True, default='cover_pics/default.jpg', null=True, upload_to='cover_pics/')),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1, null=True)),
                ('userUID', models.CharField(blank=True, editable=False, max_length=100, null=True, unique=True)),
                ('role', models.CharField(choices=[('Member', 'Member'), ('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Staff', 'Staff'), ('Owner', 'Owner'), ('VIP', 'VIP')], default='Member', max_length=50)),
                ('account_type', models.CharField(choices=[('classic', 'classic'), ('google', 'google')], default='classic', max_length=50)),
                ('third_party_jwt', models.CharField(blank=True, default='', max_length=3000, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='userRating',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ratingMessage', models.CharField(max_length=1000)),
                ('rating', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSavedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('userUID', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('isSaved', models.BooleanField(blank=True, default=True)),
                ('saved_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('book', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.bookslist')),
            ],
        ),
    ]
