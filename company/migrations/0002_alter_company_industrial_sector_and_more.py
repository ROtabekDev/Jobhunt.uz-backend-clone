# Generated by Django 4.1.4 on 2023-01-02 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_social_networks_social_network_id_and_more'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='industrial_sector',
            field=models.ManyToManyField(blank=True, to='main.indisturial_sector'),
        ),
        migrations.AlterField(
            model_name='company',
            name='speciality',
            field=models.ManyToManyField(blank=True, to='main.speciality'),
        ),
        migrations.AlterField(
            model_name='company',
            name='vacancy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.vacancy', verbose_name='Bo`sh ish o`rni'),
        ),
        migrations.AlterField(
            model_name='company',
            name='web_page',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Web sahifa'),
        ),
    ]
