# Generated by Django 5.0.5 on 2024-05-09 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamburgueria', '0003_additionalfree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalfree',
            name='category',
        ),
        migrations.AddField(
            model_name='additionalfree',
            name='category_type',
            field=models.CharField(blank=True, choices=[('MEAT', 'Adicional de Carne'), ('SAUCE', 'Adicional de Molho')], max_length=100, null=True),
        ),
    ]