# Generated by Django 5.0.5 on 2024-05-09 01:03

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgueria', '0002_category_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalFree',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='additional_category', to='hamburgueria.category')),
            ],
        ),
    ]
