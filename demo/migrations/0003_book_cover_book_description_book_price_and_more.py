# Generated by Django 4.1.7 on 2025-03-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
