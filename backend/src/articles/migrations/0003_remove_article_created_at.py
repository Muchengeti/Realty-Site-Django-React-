# Generated by Django 2.2.3 on 2019-07-15 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
    ]
