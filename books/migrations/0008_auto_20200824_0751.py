# Generated by Django 3.1 on 2020-08-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200824_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(choices=[('翔泳社', '翔泳社'), ('技術評論社', '技術評論社'), ('秀和システム', '秀和システム'), ('SBクリエイティブ', 'SBクリエイティブ'), ('日経BP', '日経BP')], max_length=50, verbose_name='出版社'),
        ),
    ]
