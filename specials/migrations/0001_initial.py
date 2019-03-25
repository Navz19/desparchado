# Generated by Django 2.0.13 on 2019-03-25 20:01

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0014_auto_20190325_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Está publicado')),
                ('image', models.ImageField(blank=True, null=True, upload_to='specials', verbose_name='Background Image')),
                ('description', models.TextField(default='', verbose_name='Descripción')),
                ('related_events', models.ManyToManyField(blank=True, related_name='specials', to='events.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
