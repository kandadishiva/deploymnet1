# Generated by Django 4.1.5 on 2023-03-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_order_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='calc.tag'),
        ),
    ]
