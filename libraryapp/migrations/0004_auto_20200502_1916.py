# Generated by Django 3.0.5 on 2020-05-02 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_auto_20200502_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn_number',
            new_name='isbn',
        ),
    ]
