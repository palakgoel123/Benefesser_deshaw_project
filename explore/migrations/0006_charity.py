# Generated by Django 3.2.3 on 2022-03-12 10:01

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('explore', '0005_delete_charity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=50)),
                ('charity_theme', models.CharField(max_length=250)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('pic_link', models.CharField(max_length=1000)),
                ('charity_id', models.CharField(max_length=7, primary_key=sqlalchemy.sql.expression.true, serialize=False)),
            ],
        ),
    ]
