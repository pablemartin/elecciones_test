# Generated by Django 4.2.7 on 2023-11-29 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0009_alter_vote_party_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='party_number',
            new_name='political_party',
        ),
    ]
