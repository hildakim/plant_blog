# Generated by Django 3.2 on 2021-05-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_title', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField()),
                ('log_body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='log/')),
            ],
        ),
    ]