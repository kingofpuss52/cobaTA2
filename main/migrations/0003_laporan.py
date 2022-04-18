# Generated by Django 4.0.3 on 2022-04-18 04:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pertanyaan_jawaban'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laporan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_laporan', models.FileField(upload_to='documents/')),
                ('tanggal_upload', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]