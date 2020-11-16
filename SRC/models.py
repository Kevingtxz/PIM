from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    initials = models.CharField(max_length=2, blank=True, null=True)

class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, blank=True, null=True)

class Region(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)

class Elo(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)

EDUCATIONS = [
    ('M', 'Master'),
    ('H', 'High School'),
    ('P', 'Phd'),
    ('D', 'Degree'),
    ('T', 'Technical'),
    ('F', 'Fundamental'),
]

class Mentor(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default='profile1.png', blank=True, null=True)
    birth = models.CharField(max_length=8, blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    laters	= models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    about_me = models.CharField(max_length=5000, blank=True, null=True)
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS, blank=True, null=True)
    focus_areas = models.CharField(max_length=5000, blank=True, null=True)
    years_experience = models.IntegerField(default=0, blank=True, null=True)
    is_public = models.BooleanField(default=True, blank=True, null=True)
    points_general = models.IntegerField(default=0, blank=True, null=True)
    
    elo = models.ForeignKey(Elo, on_delete=models.PROTECT, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)


class Poster(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    mentor = models.OneToOneField(Mentor, null=True, blank=True, on_delete=models.CASCADE)

class Content(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_public = models.BooleanField(default=True)
    poster = models.ForeignKey(Poster, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    region = models.ForeignKey(Region, null= True, on_delete=models.SET_NULL)
    elo = models.ForeignKey(Elo, on_delete=models.SET_NULL, null=True, blank=True)

class Mission(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=200, blank=True)
    region = models.ForeignKey(Region, null= True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=1500, blank=True, null=True)
    poster = models.ForeignKey(Poster, null=True, blank=True, on_delete=models.CASCADE)
    elo = models.ForeignKey(Elo, on_delete=models.SET_NULL, null=True, blank=True)

class Commentary(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    is_public = models.BooleanField(default=False)
    mentor = models.ForeignKey(Mentor, null=True, blank=True, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, null=True, blank=True, on_delete=models.CASCADE)
    poster = models.ForeignKey(Poster, null=True, blank=True, on_delete=models.CASCADE)

class Trophy(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    pontos = models.IntegerField(default=500, blank=True)
    elo = models.ForeignKey(Elo, on_delete=models.SET_NULL, null=True, blank=True)

    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    poster = models.ForeignKey(Poster, null=True, blank=True, on_delete=models.CASCADE)


class Vote(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    mentor = models.ForeignKey(Mentor, null=True, blank=True, on_delete=models.CASCADE)
    poster = models.ForeignKey(Poster, null=True, blank=True, on_delete=models.CASCADE)
    vote_support = models.BooleanField(default=False, blank=True)
    vote_engagement = models.BooleanField(default=False, blank=True)
    vote_knowledge = models.BooleanField(default=False, blank=True)
    vote_communication = models.BooleanField(default=False, blank=True)
    vote_good_to_work = models.BooleanField(default=False, blank=True)