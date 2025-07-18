# Generated by Django 5.0.4 on 2025-07-17 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='relationship_app.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='library',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='librarian', to='relationship_app.library'),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
