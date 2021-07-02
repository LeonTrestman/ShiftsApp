# Generated by Django 3.2.4 on 2021-07-02 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shifts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='weekly_schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friday_first_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='friday_first_user', to=settings.AUTH_USER_MODEL)),
                ('friday_second_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='friday_second_user', to=settings.AUTH_USER_MODEL)),
                ('monday_first_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='monday_first_user', to=settings.AUTH_USER_MODEL)),
                ('monday_second_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='monday_second_user', to=settings.AUTH_USER_MODEL)),
                ('saturday_first_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='saturday_first_user', to=settings.AUTH_USER_MODEL)),
                ('saturday_second_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='saturday_second_user', to=settings.AUTH_USER_MODEL)),
                ('sunday_first_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sunday_first_user', to=settings.AUTH_USER_MODEL)),
                ('sunday_second_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sunday_second_user', to=settings.AUTH_USER_MODEL)),
                ('thursday_first_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='thursday_first_user', to=settings.AUTH_USER_MODEL)),
                ('thursday_second_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='thursday_second_user', to=settings.AUTH_USER_MODEL)),
                ('tuesday_first_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tuesday_first_user', to=settings.AUTH_USER_MODEL)),
                ('tuesday_second_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tuesday_second_user', to=settings.AUTH_USER_MODEL)),
                ('wednesday_first_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wednesday_first_user', to=settings.AUTH_USER_MODEL)),
                ('wednesday_second_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wednesday_second_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
