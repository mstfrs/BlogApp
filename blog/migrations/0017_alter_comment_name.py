# Generated by Django 4.0.2 on 2022-02-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
