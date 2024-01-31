# Generated by Django 4.2 on 2023-05-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_boutaille_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='boutaille',
            name='cap',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='boutaille',
            name='etat',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='boutaille',
            name='marque',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='boutaille',
            name='type',
            field=models.CharField(choices=[('PLASTIC', 'Plastic'), ('ALUMINIUM', 'Aluminium')], max_length=20),
        ),
    ]
