# Generated by Django 3.1.3 on 2020-12-02 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20201201_2128'),
        ('notification', '0002_notifications_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='notification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tweet.tweet'),
        ),
    ]
