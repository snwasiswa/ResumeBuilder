from django.shortcuts import render
from django.views import generic
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Education, Project, Leadership, Skill, WorkExperience
from .serializers import EducationSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView
from django.views.generic.base import TemplateResponseMixin, View
from .forms import EducationForm, WorkExperienceForm, SkillForm, ProjectForm, LeadershipForm


# Create your views here.
class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    # permission_classes = [permissions.IsAuthenticated]


class EducationList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Education.objects.all()
        return Response({'educations': queryset})


class ResumeView(generic.TemplateView):
    """View for the Education page"""
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        educations = Education.objects.all()
        context["educations"] = educations

        return context


"""The following are the CRUD operations for Education"""


class CreatorMixin(object):
    model = Education
    form_class = EducationForm

    def get_queryset(self):
        """Allows to only display or update the education objects created"""
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class EditableCreatorMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CreatorEducationMixin(CreatorMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin):
    success_url = reverse_lazy('manage_education_list')
    success_message = "The education was added successfully"


class EditableCreatorMixinEducation(CreatorEducationMixin, EditableCreatorMixin):
    template_name = 'education/management/form.html'


class ManageEducationListView(CreatorEducationMixin, ListView):
    template_name = 'education/management/list.html'
    permission_required = 'owners.view_education'


class CreateEducationView(EditableCreatorMixinEducation, CreateView):
    permission_required = 'owners.add_education'


class UpdateEducationView(EditableCreatorMixinEducation, UpdateView):
    permission_required = 'owners.change_education'
    success_message = "The education was updated successfully"


class DeleteEducationView(CreatorEducationMixin, DeleteView):
    template_name = 'education/management/delete.html'
    permission_required = 'owners.delete_education'
    success_message = "The education was deleted successfully"


class ManageEducationDetailView(DetailView, LoginRequiredMixin):
    """ View for managing education details"""

    model = Education
    template_name = 'education/management/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        educations = Education.objects.filter(owner=self.request.user)
        context["educations"] = educations

        return context


"""The following are the CRUD operations for Work Experience"""


class CreatorWorkMixin(object):
    model = WorkExperience
    form_class = WorkExperienceForm

    def get_queryset(self):
        """Allows to only display or update the work experience objects created"""
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class CreatorWorkExperienceMixin(CreatorWorkMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin):
    success_url = reverse_lazy('manage_work_experience_list')
    success_message = "The work experience was added successfully"


class EditableCreatorMixinWorkExperience(CreatorWorkExperienceMixin, EditableCreatorMixin):
    template_name = 'work_experience/management/form.html'


class ManageWorkExperienceListView(CreatorWorkExperienceMixin, ListView):
    template_name = 'work_experience/management/list.html'
    permission_required = 'owners.view_work_experience'


class CreateWorkExperienceView(EditableCreatorMixinWorkExperience, CreateView):
    permission_required = 'owners.add_work_experience'


class UpdateWorkExperienceView(EditableCreatorMixinWorkExperience, UpdateView):
    permission_required = 'owners.change_work_experience'
    success_message = "The work experience was updated successfully"


class DeleteWorkExperienceView(CreatorWorkExperienceMixin, DeleteView):
    template_name = 'work_experience/management/delete.html'
    permission_required = 'owners.delete_work_experience'
    success_message = "The work experience was deleted successfully"


class ManageWorkExperienceDetailView(DetailView, LoginRequiredMixin):
    """ View for managing work experience details"""

    model = WorkExperience
    template_name = 'work_experience/management/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work_experiences = WorkExperience.objects.filter(owner=self.request.user)
        context["work_experiences"] = work_experiences

        return context


"""The following are the CRUD operations for Skill"""


class CreatorMixin(object):
    model = Skill
    form_class = SkillForm

    def get_queryset(self):
        """Allows to only display or update the skill objects created"""
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class CreatorSkillMixin(CreatorMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin):
    success_url = reverse_lazy('manage_skill_list')
    success_message = "The skill was added successfully"


class EditableCreatorMixinSkill(CreatorEducationMixin, EditableCreatorMixin):
    template_name = 'skill/management/form.html'


class ManageSkillListView(CreatorSkillMixin, ListView):
    template_name = 'skill/management/list.html'
    permission_required = 'owners.view_skill'


class CreateSkillView(EditableCreatorMixinSkill, CreateView):
    permission_required = 'owners.add_skill'


class UpdateSkillView(EditableCreatorMixinSkill, UpdateView):
    permission_required = 'owners.change_skill'
    success_message = "The skill was updated successfully"


class DeleteSkillView(CreatorSkillMixin, DeleteView):
    template_name = 'skill/management/delete.html'
    permission_required = 'owners.delete_skill'
    success_message = "The skill was deleted successfully"


class ManageSkillDetailView(DetailView, LoginRequiredMixin):
    """ View for managing skill details"""

    model = Skill
    template_name = 'skill/management/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skills = Skill.objects.filter(owner=self.request.user)
        context["skills"] = skills

        return context


"""The following are the CRUD operations for Leadership"""


class CreatorMixin(object):
    model = Leadership
    form_class = LeadershipForm

    def get_queryset(self):
        """Allows to only display or update the leadership objects created"""
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class CreatorLeadershipMixin(CreatorMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin):
    success_url = reverse_lazy('manage_leadership_list')
    success_message = "The leadership role was added successfully"


class EditableCreatorMixinLeadership(CreatorLeadershipMixin, EditableCreatorMixin):
    template_name = 'leadership/management/form.html'


class ManageLeadershipListView(CreatorLeadershipMixin, ListView):
    template_name = 'leadership/management/list.html'
    permission_required = 'owners.view_leadership'


class CreateLeadershipView(EditableCreatorMixinLeadership, CreateView):
    permission_required = 'owners.add_leadership'


class UpdateLeadershipView(EditableCreatorMixinLeadership, UpdateView):
    permission_required = 'owners.change_leadership'
    success_message = "The leadership role was updated successfully"


class DeleteLeadershipView(CreatorLeadershipMixin, DeleteView):
    template_name = 'leadership/management/delete.html'
    permission_required = 'owners.delete_leadership'
    success_message = "The leadership role was deleted successfully"


class ManageLeadershipDetailView(DetailView, LoginRequiredMixin):
    """ View for managing leadership details"""

    model = Leadership
    template_name = 'leadership/management/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        leaderships = Leadership.objects.filter(owner=self.request.user)
        context["leaderships"] = leaderships

        return context


"""The following are the CRUD operations for Project"""


class CreatorMixin(object):
    model = Project
    form_class = ProjectForm

    def get_queryset(self):
        """Allows to only display or update the project objects created"""
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class CreatorProjectMixin(CreatorMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin):
    success_url = reverse_lazy('manage_project_list')
    success_message = "The project was added successfully"


class EditableCreatorMixinProject(CreatorProjectMixin, EditableCreatorMixin):
    template_name = 'project/management/form.html'


class ManageProjectListView(CreatorProjectMixin, ListView):
    template_name = 'project/management/list.html'
    permission_required = 'owners.view_project'


class CreateProjectView(EditableCreatorMixinProject, CreateView):
    permission_required = 'owners.add_project'


class UpdateProjectView(EditableCreatorMixinProject, UpdateView):
    permission_required = 'owners.change_project'
    success_message = "The education was updated successfully"


class DeleteProjectView(CreatorProjectMixin, DeleteView):
    template_name = 'project/management/delete.html'
    permission_required = 'owners.delete_project'
    success_message = "The project was deleted successfully"


class ManageProjectDetailView(DetailView, LoginRequiredMixin):
    """ View for managing project details"""

    model = Project
    template_name = 'project/management/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.filter(owner=self.request.user)
        context["projects"] = projects

        return context





