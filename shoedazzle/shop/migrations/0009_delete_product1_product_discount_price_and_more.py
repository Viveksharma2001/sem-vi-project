# Generated by Django 4.1.2 on 2023-01-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product1',
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MS', 'Mens shoes'), ('WS', 'Womens shoes'), ('BS', 'Boys shoes'), ('GS', 'Girls shoes')], max_length=2),
        ),
    ]