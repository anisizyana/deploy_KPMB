# Generated by Django 4.0.5 on 2023-08-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(),
        ),
    ]
