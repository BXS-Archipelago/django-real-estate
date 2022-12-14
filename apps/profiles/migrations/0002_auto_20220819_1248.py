# Generated by Django 3.2.7 on 2022-08-19 11:48

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='License',
        ),
        migrations.AddField(
            model_name='profile',
            name='license',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Real Estate license'),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='say something about yourself', verbose_name='About me'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Nairobi', max_length=180, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default='KE', max_length=2, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=20, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_buyer',
            field=models.BooleanField(default=False, help_text='Are you looking to Buy a Property?', verbose_name='Buyer'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_seller',
            field=models.BooleanField(default=False, help_text='Are you looking to sell a property?', verbose_name='Seller'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+41524204242', max_length=30, region=None, verbose_name='Phone Number'),
        ),
    ]
