# Generated by Django 4.2.8 on 2024-01-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('st_pull_request_url', models.CharField(max_length=1000)),
                ('e2e_uat_pull_request_url', models.CharField(max_length=1000)),
                ('main_pull_request_url', models.CharField(max_length=1000)),
                ('source_branch', models.CharField(max_length=255)),
                ('target_branch', models.CharField(max_length=255)),
                ('pull_request_id', models.IntegerField()),
            ],
        ),
    ]
