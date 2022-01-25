# Generated by Django 4.0.1 on 2022-01-21 20:41

from django.db import migrations, models
import watchlist.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default='', null=True, validators=[watchlist.validators.MinValueValidator(1.0), watchlist.validators.MaxValueValidator(10.0)])),
                ('votes', models.IntegerField(blank=True, null=True, validators=[watchlist.validators.MinValueValidator(1000), watchlist.validators.MaxValueValidator(2528513)])),
                ('genre', models.CharField(blank=True, choices=[('', ''), ('drama', 'Drama'), ('comedy', 'Comedy'), ('documentary', 'Documentary'), ('horror', 'Horror'), ('adventure', 'Adventure'), ('mystery', 'Mystery'), ('romance', 'Romance'), ('musical', 'Musical'), ('western', 'Western'), ('thriller', 'Thriller'), ('crime', 'Crime'), ('war', 'War'), ('animation', 'Animation'), ('fantasy', 'Fantasy'), ('family', 'Family'), ('biography', 'Biography'), ('music', 'Music'), ('action', 'Action'), ('sci-fi', 'Sci-Fi'), ('history', 'History'), ('sport', 'Sport'), ('adult', 'Adult'), ('short', 'Short'), ('news', 'News'), ('talk-show', 'Talk-Show'), ('reality-tv', 'Reality-TV'), ('game-show', 'Game-Show')], default='', max_length=32, null=True)),
                ('prod_year', models.IntegerField(blank=True, default='', null=True, validators=[watchlist.validators.MinValueValidator(1960), watchlist.validators.MaxValueValidator(2022)])),
                ('role', models.CharField(blank=True, choices=[('', ''), ('actor', 'Actor'), ('actress', 'Actress'), ('director', 'Director')], default='', max_length=16, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('birth_year', models.IntegerField(blank=True, default='', null=True, validators=[watchlist.validators.MinValueValidator(1900), watchlist.validators.MaxValueValidator(2022)])),
                ('number_of_movies_to_choose', models.IntegerField(validators=[watchlist.validators.MinValueValidator(1), watchlist.validators.MaxValueValidator(30)])),
            ],
        ),
    ]
