# Generated by Django 3.1.3 on 2021-01-15 14:34

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Руководитель'), (3, 'Проверяющий'), (4, 'Менеджер')], null=True, verbose_name='Уровень доступа')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('personal_id', models.AutoField(primary_key=True, serialize=False)),
                ('ext_id', models.IntegerField(blank=True, null=True, verbose_name='Расширенный ID')),
                ('full_name', models.CharField(max_length=30, verbose_name='ФИО')),
                ('birth_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата рождения')),
                ('position', models.CharField(blank=True, max_length=30, null=True, verbose_name='Должность')),
                ('punishment', models.IntegerField(blank=True, null=True, verbose_name='Дисциплинарные взыскания')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('tests_id', models.AutoField(primary_key=True, serialize=False)),
                ('expected_time', models.DateTimeField(blank=True, null=True, verbose_name='Назначенное время теста')),
                ('result_time', models.DateTimeField(blank=True, null=True, verbose_name='Фактическое время сдачи теста')),
                ('result', models.BooleanField(choices=[(False, 'Провален'), (True, 'Успешно')], default=False, verbose_name='Результат')),
                ('personal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.personal')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
                'ordering': ['-result_time'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_pub', models.DateField(auto_now=True, db_index=True, verbose_name='Дата публикации')),
                ('data_photo', models.ImageField(blank=True, null=True, upload_to='static/poll', verbose_name='Фото')),
                ('personal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.personal')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
