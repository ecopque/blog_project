# Generated by Django 5.1 on 2024-09-13 00:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('excerpt', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=False, help_text='This field must be checked for the post to be displayed publicly.')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='post/%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='Display the cover image also within the post content?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
