# Generated by Django 5.2.4 on 2025-07-30 16:18

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time last updated.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique order identifier', primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', help_text='Current status of the order', max_length=20)),
                ('is_assigned', models.BooleanField(default=False, help_text='Whether the order is currently assigned to a staff member')),
                ('assigned_at', models.DateTimeField(blank=True, help_text='When the order was assigned to staff', null=True)),
                ('notes', models.TextField(blank=True, help_text='Internal notes about the order')),
                ('creator', models.ForeignKey(blank=True, help_text='User who placed the order', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('staff_orders_handler', models.ForeignKey(blank=True, help_text="Staff member assigned to work on this order. Only users with the 'ORDERS_OPERATOR' group can be assigned orders to handle.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique order item identifier', primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1, help_text='Quantity of this item in the order')),
                ('price_at_time', models.DecimalField(blank=True, decimal_places=2, help_text='Price of the item when the order was placed (for historical accuracy)', max_digits=10, null=True)),
                ('is_completed', models.BooleanField(default=False, help_text='Whether this item has been completed or fulfilled')),
                ('item', models.ForeignKey(help_text='The item being ordered', on_delete=django.db.models.deletion.CASCADE, to='stock.stockitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
            ],
            options={
                'unique_together': {('order', 'item')},
            },
        ),
    ]
