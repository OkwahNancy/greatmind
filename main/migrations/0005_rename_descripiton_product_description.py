# Generated by Django 4.1.7 on 2023-03-03 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descripiton',
            new_name='description',
        ),
    ]