from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    initials = models.CharField(max_length=2)

    def __str__(self):
        return self.initials

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Region(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Address(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    neighborhood = models.CharField(max_length=200)
    number = models.CharField(max_length=20, blank=True, null=True)
    complement = models.CharField(max_length=200, blank=True, null=True)
    
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.neighborhood


class StandardUser(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default='profile1.png', blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    birth = models.CharField(max_length=8, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    about_me = models.CharField(max_length=5000, blank=True, null=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)


class News(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    pic = models.ImageField(default='New.png', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=400, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    poster = models.CharField(max_length=200, blank=True, null=True)
    
    standard_user_poster = models.ForeignKey(User, on_delete=models.CASCADE)


class MasteryArea(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200)
    explanation = models.CharField(max_length=2000, blank=True, null=True)

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
    education_Level = models.CharField(max_length=1, choices=EDUCATIONS)
    education = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    latters	= models.CharField(max_length=200, blank=True, null=True)
    
    mastery_area = models.ForeignKey(MasteryArea, blank=True, null=True, on_delete=models.SET_NULL)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    carrear = models.OneToOneField('Carrear', on_delete=models.CASCADE)


class DaysUsing(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Carrear(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    days_working = models.ForeignKey(DaysUsing, on_delete=models.CASCADE)
    position_region_ranking = models.IntegerField(blank=True)
    position_ranking = models.IntegerField(blank=True)
    points_general = models.IntegerField(blank=True)


class Page(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.CharField(max_length=1500, blank=True, null=True)

class Content(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    pages = models.ManyToManyField(Page)


class Elo(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    mentors = models.ManyToManyField(Mentor)
    contents = models.ManyToManyField(Content)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        abstract = True

class Bronze(Elo):
    name = models.CharField(max_length=6, default='Bronze')

class Silver(Elo):
    name = models.CharField(max_length=6, default='Silver')

class Gold(Elo):
    name = models.CharField(max_length=4, default='Gold')


class Commentary(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    text = models.CharField(max_length=500)
    is_public = models.BooleanField(default=False)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, blank=True)
    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE, blank=True)


class Vote(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, blank=True)
    standard_user = models.ForeignKey(StandardUser, on_delete=models.CASCADE, blank=True)
    class Meta:
        abstract = True

class CharismVote(Vote):
    pass

class EngagementVote(Vote):
    pass

class PerseveranceVote(Vote):
    pass

class EthicsVote(Vote):
    pass

class BusinessStrategyVote(Vote):
    pass

class SalesVote(Vote):
    pass

class CommunicationVote(Vote):
    pass

class NetworkingVote(Vote):
    pass

class KnowledgeVote(Vote):
    pass

class FocusVote(Vote):
    pass