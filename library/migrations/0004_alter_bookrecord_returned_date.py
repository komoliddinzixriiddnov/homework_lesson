# Generated by Django 5.0.3 on 2024-03-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_bookrecord_returned_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='returned_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
