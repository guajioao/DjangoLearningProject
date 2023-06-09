# Generated by Django 3.2.15 on 2023-03-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfdemo', '0006_alter_student_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='书籍名称')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('pub_data', models.DateField(verbose_name='出版日期')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=32)),
            ],
        ),
    ]
