from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .filters import *

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            mentor = Mentor.objects.create(user=user)
            Poster.objects.create(mentor=mentor)
            messages.success(request, 'Account was created for' + username)
            
            return redirect('login')

    context = {'form': form}
    return render(request, 'src/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('missions')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, "src/login.html", context)
     

def logoutUser(request):
    logout(request)
    return redirect('login')

def myProfile(request):
    form = MentorFormUpdate()
    if request.method == 'PUT':
        mentor = Mentor.objects.get(id=request.id)
        if MentorFormUpdate.nickname:
            mentor.nickname = MentorFormUpdate.nickname
        if MentorFormUpdate.education:
            mentor.education = MentorFormUpdate.education
        if MentorFormUpdate.linkedin:
            mentor.linkedin = MentorFormUpdate.linkedin
        if MentorFormUpdate.laters:
            mentor.laters = MentorFormUpdate.laters
        if MentorFormUpdate.phone:
            mentor.phone = MentorFormUpdate.phone
        if MentorFormUpdate.telegram:
            mentor.telegram = MentorFormUpdate.telegram
        if MentorFormUpdate.about_me:
            mentor.about_me = MentorFormUpdate.about_me
        if MentorFormUpdate.education_Level:
            mentor.education_Level = MentorFormUpdate.education_Level
        if MentorFormUpdate.focus_areas:
            mentor.focus_areas = MentorFormUpdate.focus_areas
        if MentorFormUpdate.years_experience:
            mentor.years_experience = MentorFormUpdate.years_experience
        mentor.save()
    context = {
        'form':form
    }



def home(request):
    content = Content.objects.get(id=1)
    context = {
        'content' : content,
    }
    return render(request, 'src/home.html', context)


@login_required(login_url='login')
def course(request):
    contents = Content.objects.all()
    context = {
        'contents' : contents,
    }
    return render(request, 'src/course.html', context)

def mentors(request):
    filter = MentorFilter(
        request.GET, queryset=Mentor.objects.filter(is_public=True)
    )
    paginator = Paginator(filter.qs, 10)
    page = request.GET.get('page')
    try:
        mentors = paginator.page(page)
    except PageNotAnInteger:
        mentors = paginator.page(1)
    except EmptyPage:
        mentors = paginator.page(paginator.num_pages)
    mentors_num = len(mentors)
    context = {
        'page': page,
        'mentors': mentors,
        'filter': filter,
        'mentors_num': mentors_num,
    }
    return render(request, 'src/mentors.html, context')


def rankingMentors(request):
    filter = MentorFilter(
        request.GET, queryset= Count('points_general', filter=Mentor(points_general__rating__gt=5))
    )
    paginator = Paginator(filter.qs, 10)
    page = request.GET.get('page')
    try:
        mentors = paginator.page(page)
    except PageNotAnInteger:
        carrears = paginator.page(1)
    except EmptyPage:
        mentors = paginator.page(paginator.num_pages)
    context = {
        'mentors' : mentors,
    }
    return render(request, 'src/rankingmentors.html', context)


def mentorProfile(request, id):
    mentor = Mentor.objects.get(id=id)
    form = VoteForm()

    vote_support = Vote.objects.filter(vote_support=True).count()
    vote_engagement = Vote.objects.filter(vote_engagement=True).count()
    vote_knowledge = Vote.objects.filter(vote_knowledge=True).count()
    vote_communication = Vote.objects.filter(vote_communication=True).count()
    vote_good_to_work = Vote.objects.filter(vote_good_to_work=True).count()

    if request.method == 'POST':
        poster = Poster.objects.get(id=request.id)
        vote = VoteSupport(mentor=mentor, poster = poster)
        vote.save()
        mentor.points_general += 10 * mentor.region.bonus
        mentor.save()
    context = {
        'mentor' : mentor,
        'form' : form,
        'support' : support,
        'engagement' : engagement,
        'knowledge' : knowledge,
        'communication' : communication,
        'good_to_work' : good_to_work,
    }
    return render(request, 'src/mentor_profile.html', context)


@login_required(login_url='login')
def missions(request):
    filter = MissionFilter(
        request.GET, queryset=Mission.objects.filter(is_public=True)
    )
    paginator = Paginator(filter.qs, 5)
    page = request.GET.get('page')
    try:
        missions = paginator.page(page)
    except PageNotAnInteger:
        missions = paginator.page(1)
    except EmptyPage:
        missions = paginator.page(paginator.num_pages)
    missions_num = len(missions)
    context = {
        'page': page,
        'missions': missions,
        'filter': filter,
        'missions_num': missions_num,
    }
    return render(request, 'src/missions.html', context)