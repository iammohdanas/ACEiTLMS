# Generated by Django 4.2.5 on 2024-01-23 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_language_course_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='deadline',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
