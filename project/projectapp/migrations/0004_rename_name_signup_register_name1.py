# Generated by Django 4.1.4 on 2023-01-05 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projectapp", "0003_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="signup_register", old_name="name", new_name="name1",
        ),
    ]
