# Generated by Django 2.2 on 2019-03-21 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Label', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('qid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('processed', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
