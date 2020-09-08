# Generated by Django 3.1.1 on 2020-09-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('pup_name', models.CharField(max_length=100)),
                ('age', models.DateField()),
                ('primary_lang', models.CharField(max_length=100)),
                ('secondary_lang', models.CharField(max_length=100)),
                ('current_location', models.CharField(max_length=100)),
                ('relationship_status', models.CharField(max_length=100)),
                ('hashtags', models.CharField(max_length=100)),
                ('profile_img_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.TextField()),
                ('whatsapp', models.TextField()),
                ('email', models.EmailField(max_length=254, verbose_name=())),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='UserSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.TextField()),
                ('instagram', models.TextField()),
                ('furaffinity', models.TextField()),
                ('facebook', models.TextField()),
            ],
        ),
    ]
