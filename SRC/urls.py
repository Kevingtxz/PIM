from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'), 
    path('', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('mentors/', views.mentors, name='mentors'),
    path('ranking_mentors/', views.rankingMentors, name='ranking_mentors'),
    path('mentor_profile/<int:id>/', views.mentorProfile, name='mentor_profile'), 
    path('missions/', views.missions, name='missions'),    
    # path('mission_post/', views.missionPost, name='mission_post'),
]