# Generated by Django 4.1.2 on 2022-12-29 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_fname_contact_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='fname',
        ),
    ]