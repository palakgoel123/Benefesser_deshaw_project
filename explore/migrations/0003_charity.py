# Generated by Django 3.2.3 on 2022-03-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('explore', '0002_delete_charity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=50)),
                ('charity_theme', models.CharField(max_length=250)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
                ('pic_link', models.CharField(max_length=1000)),
            ],
        ),
    ]