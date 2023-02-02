from django.urls import path
from builder import views

# Patterns of different paths
urlpatterns = [

    # url for generating resume pdf
    path('resume_pdf', views.GenerateResumeView.as_view(), name='resume_pdf'),
    # Urls for different sections
    path('contact', views.ContactView.as_view(), name='contact'),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('skills', views.SkillsView.as_view(), name='skills'),
    path('educations', views.EducationView.as_view(), name='educations'),
    path('work_experiences', views.WorkExperiencesView.as_view(), name='work_experiences'),
    path('leaderships', views.LeadershipView.as_view(), name='leaderships'),
    # Urls for education
    path('educations/list/manage', views.ManageEducationListView.as_view(), name='manage_education_list'),
    path('educations/list/manage/<slug:slug>/', views.ManageEducationDetailView.as_view(),
         name='manage_education_detail'),
    path('educations/create/', views.CreateEducationView.as_view(), name='education_create'),
    path('educations/<pk>/edit/', views.UpdateEducationView.as_view(), name='education_edit'),
    path('educations/<pk>/delete/', views.DeleteEducationView.as_view(), name='education_delete'),
    # Urls for project
    path('projects/list/manage', views.ManageProjectListView.as_view(), name='manage_project_list'),
    path('projects/list/manage/<slug:slug>/', views.ManageProjectDetailView.as_view(),
         name='manage_project_detail'),
    path('projects/create/', views.CreateProjectView.as_view(), name='project_create'),
    path('projects/<pk>/edit/', views.UpdateProjectView.as_view(), name='project_edit'),
    path('projects/<pk>/delete/', views.DeleteProjectView.as_view(), name='project_delete'),
    # urls for work experiences
    path('work_experiences/list/manage', views.ManageWorkExperienceListView.as_view(),
         name='manage_work_experience_list'),
    path('work_experiences/list/manage/<slug:slug>/', views.ManageWorkExperienceDetailView.as_view(),
         name='manage_work_experience_detail'),
    path('work_experiences/create/', views.CreateWorkExperienceView.as_view(), name='work_experience_create'),
    path('work_experiences/<pk>/edit/', views.UpdateWorkExperienceView.as_view(), name='work_experience_edit'),
    path('work_experiences/<pk>/delete/', views.DeleteWorkExperienceView.as_view(), name='work_experience_delete'),
    # Urls for skill
    path('skills/list/manage', views.ManageSkillListView.as_view(), name='manage_skill_list'),
    path('skills/list/manage/<slug:slug>/', views.ManageSkillDetailView.as_view(),
         name='manage_skill_detail'),
    path('skills/create/', views.CreateSkillView.as_view(), name='skill_create'),
    path('skills/<pk>/edit/', views.UpdateSkillView.as_view(), name='skill_edit'),
    path('skills/<pk>/delete/', views.DeleteSkillView.as_view(), name='skill_delete'),
    # urls for leadership
    path('leaderships/list/manage', views.ManageLeadershipListView.as_view(), name='manage_leadership_list'),
    path('leaderships/list/manage/<slug:slug>/', views.ManageLeadershipDetailView.as_view(),
         name='manage_leadership_detail'),
    path('leaderships/create/', views.CreateLeadershipView.as_view(), name='leadership_create'),
    path('leaderships/<pk>/edit/', views.UpdateLeadershipView.as_view(), name='leadership_edit'),
    path('leaderships/<pk>/delete/', views.DeleteLeadershipView.as_view(), name='leadership_delete'),

]
