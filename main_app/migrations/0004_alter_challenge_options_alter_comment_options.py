# Generated by Django 4.1.3 on 2022-11-22 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='challenge',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
    ]