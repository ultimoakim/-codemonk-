# Generated by Django 4.1.3 on 2022-11-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_challenge_options_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.TextField(max_length=3000),
        ),
    ]