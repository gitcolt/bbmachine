# Generated by Django 2.2.3 on 2019-07-20 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subdiscovery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='domain',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subdomain',
            old_name='subdomain',
            new_name='name',
        ),
    ]
