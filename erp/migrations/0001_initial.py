# Generated by Django 4.2 on 2023-04-05 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=32)),
                ('goods_category', models.CharField(max_length=32)),
                ('stock', models.IntegerField(max_length=4)),
                ('goods_color', models.CharField(max_length=32)),
                ('goods_size', models.CharField(max_length=4)),
                ('id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'stuff',
            },
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('out_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(max_length=4)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.stuff')),
            ],
            options={
                'db_table': 'outbound',
            },
        ),
        migrations.CreateModel(
            name='Inbound',
            fields=[
                ('in_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(max_length=4)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.stuff')),
            ],
            options={
                'db_table': 'inbound',
            },
        ),
    ]
