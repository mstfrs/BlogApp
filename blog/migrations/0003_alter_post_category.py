# Generated by Django 4.0.2 on 2022-02-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('FrontEnd', 'FrontEnd'), ('BackEnd', 'BackEnd'), ('FullStack', 'FullStack')], max_length=100),
        ),
    ]