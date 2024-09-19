# Generated by Django 5.1.1 on 2024-09-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.CharField(default=1, max_length=256, verbose_name='article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/profile/nou.jpg', upload_to='images/profile', verbose_name='image'),
        ),
    ]