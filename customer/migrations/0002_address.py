# Generated by Django 3.2.7 on 2021-10-14 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50, unique=True)),
                ('country', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
