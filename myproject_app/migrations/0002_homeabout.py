# Generated by Django 3.0.3 on 2020-02-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]