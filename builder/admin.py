from django.contrib import admin
from .models import Education, Project, Skill, Leadership, WorkExperience


# Register your models here.
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'school', 'degree', 'major',)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'position', 'description_or_role',)


@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rating')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'year')
    readonly_fields = ('slug',)
