# Generated by Django 3.1 on 2020-08-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBNコード')),
                ('title', models.CharField(max_length=100, verbose_name='署名')),
                ('price', models.IntegerField(default=0, verbose_name='価格')),
                ('publisher', models.CharField(choices=[('SBクリエイティブ', 'SBクリエイティブ'), ('秀和システム', '秀和システム'), ('技術評論社', '技術評論社'), ('翔泳社', '翔泳社'), ('日経BP', '日経BP')], max_length=50, verbose_name='出版社')),
                ('published', models.DateField(verbose_name='刊行日')),
            ],
        ),
    ]
