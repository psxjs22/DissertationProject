# Generated by Django 4.2.4 on 2023-08-12 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsentForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('initials', models.CharField(max_length=10)),
                ('date', models.DateField(default='2023-01-01')),
                ('signed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consent_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='basicapp.consentform')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('summary', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('authenticity', models.CharField(max_length=10)),
                ('explanation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('response', models.CharField(max_length=10)),
                ('confidence', models.PositiveIntegerField()),
                ('reason', models.TextField()),
                ('attempt', models.PositiveIntegerField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicapp.participant')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicapp.question')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='treatment_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicapp.treatmentgroup'),
        ),
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('ethnicity', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicapp.participant')),
            ],
        ),
    ]
