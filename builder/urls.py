from django.contrib import admin
from django.urls import path, include
from builder import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.routers import DefaultRouter

app_name = 'builder'
# # Build url dynamically using router
router = routers.DefaultRouter()
router.register(app_name, views.EducationViewSet)


# Patterns of different paths
urlpatterns = [

    path('', views.ResumeView.as_view(), name='resume'),
    path('api/', include(router.urls)),
    # Urls for education
    path('education/list/manage', views.ManageEducationListView.as_view(), name='manage_education_list'),
    path('education/list/manage/<slug:slug>/', views.ManageEducationDetailView.as_view(),
         name='manage_education_detail'),
    path('education/create/', views.CreateEducationView.as_view(), name='education_create'),
    path('education/<pk>/edit/', views.UpdateEducationView.as_view(), name='education_edit'),
    path('education/<pk>/delete/', views.DeleteEducationView.as_view(), name='education_delete'),
    # Urls for project
    path('project/list/manage', views.ManageProjectListView.as_view(), name='manage_project_list'),
    path('project/list/manage/<slug:slug>/', views.ManageProjectDetailView.as_view(),
         name='manage_project_detail'),
    path('project/create/', views.CreateProjectView.as_view(), name='project_create'),
    path('project/<pk>/edit/', views.UpdateProjectView.as_view(), name='project_edit'),
    path('project/<pk>/delete/', views.DeleteProjectView.as_view(), name='project_delete'),
    # urls for work experiences
    path('work_experience/list/manage', views.ManageWorkExperienceListView.as_view(), name='manage_work_experience_list'),
    path('work_experience/list/manage/<slug:slug>/', views.ManageWorkExperienceDetailView.as_view(),
         name='manage_work_experience_detail'),
    path('work_experience/create/', views.CreateWorkExperienceView.as_view(), name='work_experience_create'),
    path('work_experience/<pk>/edit/', views.UpdateWorkExperienceView.as_view(), name='work_experience_edit'),
    path('work_experience/<pk>/delete/', views.DeleteWorkExperienceView.as_view(), name='work_experience_delete'),
    # Urls for skill
    path('skill/list/manage', views.ManageSkillListView.as_view(), name='manage_skill_list'),
    path('education/list/manage/<slug:slug>/', views.ManageSkillDetailView.as_view(),
         name='manage_skill_detail'),
    path('skill/create/', views.CreateSkillView.as_view(), name='skill_create'),
    path('skill/<pk>/edit/', views.UpdateSkillView.as_view(), name='skill_edit'),
    path('skill/<pk>/delete/', views.DeleteSkillView.as_view(), name='skill_delete'),
    # urls for leadership
    path('leadership/list/manage', views.ManageLeadershipListView.as_view(), name='manage_leadership_list'),
    path('leadership/list/manage/<slug:slug>/', views.ManageLeadershipDetailView.as_view(),
         name='manage_leadership_detail'),
    path('leadership/create/', views.CreateLeadershipView.as_view(), name='leadership_create'),
    path('leadership/<pk>/edit/', views.UpdateLeadershipView.as_view(), name='leadership_edit'),
    path('leadership/<pk>/delete/', views.DeleteLeadershipView.as_view(), name='leadership_delete'),

]
