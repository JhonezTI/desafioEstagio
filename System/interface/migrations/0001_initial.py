# Generated by Django 4.0.3 on 2022-03-25 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kitnet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumKitnet',  models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14)),
                ('Tam_Kitnet', models.CharField(choices=[('Pequeno', 'Pequeno'), ('Medio', 'Medio'), ('Gramde', 'Grande')], max_length=7)),
                ('Inadimplente', models.BooleanField()),
                ('T_Inadimplente', models.CharField(max_length=14)),
                ('Valor_Imovel', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
