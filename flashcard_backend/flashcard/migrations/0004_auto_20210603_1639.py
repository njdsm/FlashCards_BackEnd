# Generated by Django 3.1.8 on 2021-06-03 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20210603_1622'),
        ('flashcard', '0003_auto_20210603_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='collection',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.collection'),
        ),
    ]