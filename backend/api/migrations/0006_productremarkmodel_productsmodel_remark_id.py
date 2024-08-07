# Generated by Django 5.0.6 on 2024-07-08 02:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_productsmodel_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRemarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='remark_ID',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='api.productremarkmodel'),
            preserve_default=False,
        ),
    ]
