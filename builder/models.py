from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from users.models import User


# Create your models here.

class Education(models.Model):
    """Model for the education section"""

    owner = models.ForeignKey(User, related_name='education_added', on_delete=models.CASCADE)
    school = models.CharField(blank=False, null=False, max_length=255)
    degree = models.CharField(blank=False, null=False, max_length=255)
    major = models.CharField(blank=False, null=False, max_length=255)
    minor = models.CharField(blank=True, null=True, max_length=255)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=4.00,
                              validators=[MinValueValidator(Decimal(0.00))])
    scale = models.DecimalField(max_digits=3, decimal_places=2, default=4.00,
                                validators=[MinValueValidator(Decimal(0.00))])
    year = models.CharField(blank=False, null=False, max_length=255)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.school)
        super(Education, self).save(*args, **kwargs)

    def __str__(self):
        return self.school


class WorkExperience(models.Model):
    """Model for the education section"""
    owner = models.ForeignKey(User, related_name='experience_added', on_delete=models.CASCADE)
    company = models.CharField(blank=False, null=False, max_length=255)
    position = models.CharField(blank=False, null=False, max_length=255)
    description_or_role = models.CharField(blank=False, null=False, max_length=255)
    year = models.CharField(blank=False, null=False, max_length=255)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'WorkExperience'
        verbose_name_plural = 'WorkExperiences'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.position)
        super(WorkExperience, self).save(*args, **kwargs)

    def __str__(self):
        return self.position


class Skill(models.Model):
    """Model for skills"""
    owner = models.ForeignKey(User, related_name='skill_added', on_delete=models.CASCADE)
    name = models.CharField(max_length=25, blank=True, null=True)
    image = models.FileField(upload_to="logos", null=True, blank=True)
    rating = models.IntegerField(default=4, null=True, blank=True)
    is_hard_skill = models.BooleanField(default=False)
    is_soft_skill = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Skill, self).save(*args, **kwargs)

    @property
    def get_logo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216413/media/logos/default-thumb_dn1xzg.png"


class Leadership(models.Model):
    """Model for user campus involvement or leadership"""
    owner = models.ForeignKey(User, related_name='leadership_added', on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=500)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(blank=True, null=True)
    description_or_role = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Leadership'
        verbose_name_plural = 'Leaderships'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Leadership, self).save(*args, **kwargs)


class Project(models.Model):
    """Model for user portfolio"""
    owner = models.ForeignKey(User, related_name='project_added', on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=250)
    image = models.ImageField(blank=True, null=True, upload_to="portfolios")
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(blank=True, null=True, max_length=250)
    role = RichTextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    is_side_project = models.BooleanField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    year = models.CharField(blank=True, null=True, max_length=70)
    technology = models.CharField(blank=True, null=True, max_length=1000)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/project/{self.slug}"

    @property
    def get_logo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "https://res.cloudinary.com/dh13i9dce/image/upload/v1642216413/media/logos/default-thumb_dn1xzg.png"
