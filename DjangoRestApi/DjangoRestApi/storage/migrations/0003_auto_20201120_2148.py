# Generated by Django 3.1.3 on 2020-11-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20201120_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='storage.Tag'),
        ),
    ]