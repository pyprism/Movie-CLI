# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_remove_movie_number_of_times_watched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movietype',
            name='movie_type',
            field=models.CharField(choices=[('Act', 'Action'), ('Ani', 'Animation'), ('Com', 'Comedy'), ('Doc', 'Documentary'), ('Fam', 'Family'), ('FN', 'Film-Noir'), ('Hor', 'Horror'), ('Mus', 'Musical'), ('Rom', 'Romance'), ('Spo', 'Sport'), ('War', 'War'), ('Adv', 'Adventure'), ('Bio', 'Biography'), ('Cri', 'Crime'), ('Dra', 'Drama'), ('Fan', 'Fantasy'), ('His', 'History'), ('Mus', 'Music'), ('Mys', 'Mystery'), ('Sci', 'Sci-Fi'), ('Thr', 'Thriller'), ('Wes', 'Western')], max_length=3),
        ),
    ]
