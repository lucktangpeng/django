# Generated by Django 3.1 on 2020-08-21 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='作者名称')),
                ('age', models.IntegerField(verbose_name='作者年龄')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='书名')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_text.type', verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_text.author', verbose_name='作者ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_text.book', verbose_name='书籍ID')),
            ],
        ),
    ]