from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Education, Skill, Project, Leadership, WorkExperience
from localflavor.us.forms import USZipCodeField
from localflavor.us.us_states import STATE_CHOICES


class EducationForm(forms.ModelForm):
    """Login form to for adding education"""

    class Meta:
        model = Education
        fields = ('school', 'major', 'minor', 'gpa', 'year',)


class WorkExperienceForm(forms.ModelForm):
    """Login form to for adding work experience"""

    class Meta:
        model = WorkExperience
        fields = ('company', 'position', 'description_or_role', 'year')


class ProjectForm(forms.ModelForm):
    """Login form to for adding a project"""

    class Meta:
        model = Project
        fields = ('name', 'image', 'description', 'role', 'is_side_project', 'year', 'technology', 'url')


class SkillForm(forms.ModelForm):
    """Login form to for adding a skill"""

    class Meta:
        model = Skill
        fields = ('name', 'image', 'rating', 'is_hard_skill', 'is_soft_skill',)


class LeadershipForm(forms.ModelForm):
    """Login form to for adding a leadership role"""

    class Meta:
        model = Leadership
        fields = ('name', 'description_or_role',)
