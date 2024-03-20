# Generated by Django 4.2.11 on 2024-03-19 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_genre_language_book_description_book_isbn_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
