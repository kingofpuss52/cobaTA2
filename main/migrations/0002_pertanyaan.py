# Generated by Django 4.0.3 on 2022-04-18 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pertanyaan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pertanyaan', models.TextField()),
                ('jenis', models.CharField(choices=[('Text', 'Text'), ('Radio', 'Radio')], default='Text', max_length=10)),
            ],
        ),
    ]