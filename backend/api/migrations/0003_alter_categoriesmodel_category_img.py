# Generated by Django 5.0.6 on 2024-06-27 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_des_productsdetailsmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriesmodel',
            name='category_img',
            field=models.ImageField(upload_to='images/categoryImg/'),
        ),
    ]