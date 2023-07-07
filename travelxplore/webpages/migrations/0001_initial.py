# Generated by Django 4.2.3 on 2023-07-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('d_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='d_id')),
                ('d_name', models.CharField(max_length=50)),
                ('d_img', models.ImageField(upload_to='images')),
                ('d_desc', models.TextField()),
                ('d_price', models.IntegerField()),
                ('d_offer', models.BooleanField(default=False)),
            ],
        ),
    ]
