# Generated by Django 4.2 on 2023-05-19 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_boutaille_cap_boutaille_etat_boutaille_marque_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boutaille',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]