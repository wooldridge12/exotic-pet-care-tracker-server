# Generated by Django 4.0.4 on 2022-06-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exoticPetCareTrackerapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meat', models.CharField(max_length=50)),
                ('fruit', models.CharField(max_length=50)),
                ('vegetable', models.CharField(max_length=50)),
                ('green', models.CharField(max_length=50)),
                ('weed', models.CharField(max_length=50)),
            ],
        ),
    ]