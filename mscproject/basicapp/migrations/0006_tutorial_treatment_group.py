# Generated by Django 4.2.4 on 2023-08-13 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0005_alter_tutorial_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='treatment_group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='basicapp.treatmentgroup'),
            preserve_default=False,
        ),
    ]
