# Generated by Django 3.2.23 on 2024-01-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20231226_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
