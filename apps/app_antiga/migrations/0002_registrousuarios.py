# Generated by Django 2.1.1 on 2018-12-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_antiga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'registro_usuarios',
            },
        ),
    ]
