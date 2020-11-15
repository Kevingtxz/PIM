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
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            mentor = Mentor.objects.create(user=user)
            Poster.objects.create(mentor=mentor)
            messages.success(request, "Account was created for " + username)
            
            return redirect("login")

    context = {"form": form}
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
            messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, "src/login.html", context)
     

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    content = Content.objects.get(id=1)
    context = {
        'content' : content,
    }
    return render(request, 'src/home.html', context)


@login_required(login_url="login")
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
        request.GET, queryset=Mentor.objects.filter(

        )
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
    if request.method == 'POST':
        poster = Poster.objects.get(id=request.id)
        vote = VoteSupport(mentor=mentor, poster = poster)        
    support = mentor.votesupport_set.all().count()
    engagement = mentor.voteengagement_set.all().count()
    knowledge = mentor.voteknowledge_set.all().count()
    communication = mentor.votecommunication_set.all().count()
    good_to_work = mentor.votegoodtowork_set.all().count()
    context = {
        'mentor' : mentor,
        'support' : support,
        'engagement' : engagement,
        'knowledge' : knowledge,
        'communication' : communication,
        'good_to_work' : good_to_work,
    }
    return render(request, 'src/mentor_profile.html', context)


@login_required(login_url="login")
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


# @login_required(login_url='login')
# def missionPost(request):
#     form = MissionForm()
#     if request.method == 'POST':
#         poster = Poster.objects.filter(mentor= request.user)
# # add poster to form
#         form = MissionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('missions/')
#     context = {
#         'form': form,
#     }
#     return render(request, 'src/mission_post.html', context)