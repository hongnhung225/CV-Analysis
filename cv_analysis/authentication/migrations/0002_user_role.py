# Generated by Django 5.1.7 on 2025-03-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('hr', 'HR'), ('cand', 'Candidate')], default='user', max_length=10),
        ),
    ]
