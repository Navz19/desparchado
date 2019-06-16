# Generated by Django 2.0.13 on 2019-06-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_event_press_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='press_articles',
            field=models.ManyToManyField(blank=True, related_name='events', to='news.PressArticle', verbose_name='Artículos de prensa'),
        ),
    ]
