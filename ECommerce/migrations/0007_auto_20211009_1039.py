# Generated by Django 3.2.7 on 2021-10-09 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ECommerce', '0006_auto_20211008_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='ECommerce.user'),
        ),
        migrations.AlterField(
            model_name='product',
            name='buy_price',
            field=models.FloatField(verbose_name='buy_price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.FloatField(verbose_name='sell_price'),
        ),
    ]