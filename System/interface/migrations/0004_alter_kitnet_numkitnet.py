# Generated by Django 4.0.3 on 2022-03-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_alter_kitnet_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitnet',
            name='NumKitnet',
            field=models.CharField(max_length=50, unique=b'I01\n'),
        ),
    ]
