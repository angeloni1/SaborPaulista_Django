# Generated by Django 4.2.9 on 2024-04-06 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_ondecomprar_options_produtofotos_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='subtitulo',
            new_name='descritivo',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='arquivo',
        ),
        migrations.AddField(
            model_name='documents',
            name='arquivo_img',
            field=models.FileField(blank=True, upload_to='anexos/', verbose_name='Imagem'),
        ),
        migrations.AddField(
            model_name='documents',
            name='arquivo_pdf',
            field=models.FileField(blank=True, upload_to='anexos/', verbose_name='PDF'),
        ),
        migrations.AddField(
            model_name='documents',
            name='arquivo_word',
            field=models.FileField(blank=True, upload_to='anexos/', verbose_name='Word'),
        ),
        migrations.AddField(
            model_name='documents',
            name='arquivo_zip',
            field=models.FileField(blank=True, upload_to='anexos/', verbose_name='Zip'),
        ),
    ]
