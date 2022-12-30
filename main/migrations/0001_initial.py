# Generated by Django 4.1.4 on 2022-12-26 10:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Pul birligi',
                'verbose_name_plural': 'Pul birliklari',
            },
        ),
        migrations.CreateModel(
            name='Indisturial_sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Sanoat soha',
                'verbose_name_plural': 'Sanoat sohalar',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Viloyat yoki shahar',
                'verbose_name_plural': 'Viloyat va shaharlar',
            },
        ),
        migrations.CreateModel(
            name='Social_network_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Ijtimoiy tarmoq',
                'verbose_name_plural': 'Ijtimoiy tarmoqlar',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
                ('for_worker', models.BooleanField(verbose_name='Ishchi uchun')),
                ('idustrial_sector_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.indisturial_sector', verbose_name='Sanoat soha')),
            ],
            options={
                'verbose_name': 'Mutaxassislik',
                'verbose_name_plural': 'Mutaxassisliklar',
            },
        ),
        migrations.CreateModel(
            name='Social_networks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='Foydalanuvchi nomi')),
                ('social_network_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.social_network_types', verbose_name='Ijtimoiy tarmoq')),
            ],
            options={
                'verbose_name': 'Ijtimoiy tarmoq',
                'verbose_name_plural': 'Ijtimoiy tarmoqlar',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nomi')),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.region', verbose_name='Viloyat yoki shahar nomi')),
            ],
            options={
                'verbose_name': 'Tuman',
                'verbose_name_plural': 'Tumanlar',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(default=uuid.uuid4, max_length=50, unique=True, verbose_name='Foydalanuvchi nomi')),
                ('phone_number', models.CharField(error_messages={'unique': 'Bu telefon nomer ro`yhatdan o`tgan!'}, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Iltimos telefon nomerni to`g`ri kiriting', regex='^[+][998]{3}?[0-9]{9}$')], verbose_name='Telefon nomer')),
                ('email', models.EmailField(max_length=254, verbose_name='Elektron pochta')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('district_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.district', verbose_name='Tumani')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('region_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region', verbose_name='Viloyat yoki shahari')),
                ('social_networs', models.ManyToManyField(to='main.social_networks', verbose_name='Ijtimoiy tarmoqlari')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Barcha foydalanuvchilar',
            },
        ),
    ]