# Generated by Django 4.1.4 on 2023-01-06 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projectapp", "0004_rename_name_signup_register_name1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="signup_register", old_name="name1", new_name="name",
        ),
    ]
