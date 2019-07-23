# Generated by Django 2.0.13 on 2019-07-23 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20190713_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(help_text='Por favor, asegúrate de que el organizador que quieres asignar al evento no existe en nuestro sistema, antes de crearlo.', related_name='events', to='events.Organizer', verbose_name='Organizadores'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(help_text='Por favor, asegúrate de que el lugar que quieres asignar al evento no existe en nuestro sistema, antes de crearlo.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='places.Place', verbose_name='Lugar'),
        ),
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=models.ManyToManyField(blank=True, help_text='Por favor, asegúrate de que el presentador/la presentadora que quieres asignar al evento no existe en nuestro sistema, antes de crearlo/crearla.', related_name='events', to='events.Speaker', verbose_name='Presentadores'),
        ),
    ]
