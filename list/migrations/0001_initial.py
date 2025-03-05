# Generated by Django 5.1.5 on 2025-03-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('teacher_name', models.CharField(max_length=50)),
                ('status', models.SmallIntegerField(default=1)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('family', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=12, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
