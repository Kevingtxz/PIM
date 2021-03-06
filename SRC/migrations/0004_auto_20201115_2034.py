# Generated by Django 3.1.1 on 2020-11-15 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20201115_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('vote_support', models.CharField(blank=True, max_length=1, null=True)),
                ('vote_engagement', models.CharField(blank=True, max_length=1, null=True)),
                ('vote_knowledge', models.CharField(blank=True, max_length=1, null=True)),
                ('vote_communication', models.CharField(blank=True, max_length=1, null=True)),
                ('vote_good_to_work', models.CharField(blank=True, max_length=1, null=True)),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='src.mentor')),
                ('poster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='src.poster')),
            ],
        ),
        migrations.RemoveField(
            model_name='voteengagement',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='voteengagement',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='votegoodtowork',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='votegoodtowork',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='voteknowledge',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='voteknowledge',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='votesupport',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='votesupport',
            name='poster',
        ),
        migrations.DeleteModel(
            name='VoteCommunication',
        ),
        migrations.DeleteModel(
            name='VoteEngagement',
        ),
        migrations.DeleteModel(
            name='VoteGoodToWork',
        ),
        migrations.DeleteModel(
            name='VoteKnowledge',
        ),
        migrations.DeleteModel(
            name='VoteSupport',
        ),
    ]
