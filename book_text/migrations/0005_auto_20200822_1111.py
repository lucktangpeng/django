# Generated by Django 3.1 on 2020-08-22 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_text', '0004_book_isdncode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isdncode',
            new_name='ISBN',
        ),
    ]
