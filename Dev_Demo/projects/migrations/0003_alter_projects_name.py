# Generated by Django 3.2.7 on 2023-06-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(db_column='projects_name', help_text='项目名称', max_length=20, unique=True, verbose_name='项目名称'),
        ),
    ]
