# Generated by Django 3.1.4 on 2020-12-09 12:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('sign_date', models.DateField(blank=True, null=True)),
                ('sign_status', models.BooleanField(default=False)),
                ('path', models.CharField(max_length=10000)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
