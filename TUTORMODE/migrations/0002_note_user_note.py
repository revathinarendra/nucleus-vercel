# Generated by Django 5.0.4 on 2024-05-13 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUTORMODE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
