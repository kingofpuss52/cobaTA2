# Generated by Django 4.0.3 on 2022-04-18 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pertanyaan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jawaban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi', models.CharField(max_length=200, null=True)),
                ('skor', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True)),
                ('kode_pertanyaan', models.ForeignKey(limit_choices_to={'jenis': 'Radio'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.pertanyaan')),
            ],
        ),
    ]
