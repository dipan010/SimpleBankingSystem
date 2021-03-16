# Generated by Django 3.0.6 on 2021-03-16 16:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('balance', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_name', to='banktransfers.Customer')),
                ('to_field', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='to_name', to='banktransfers.Customer')),
            ],
        ),
    ]
