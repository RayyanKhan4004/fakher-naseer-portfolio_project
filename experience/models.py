from django.db import models


class Experience(models.Model):
    """A single work-experience bullet point / entry."""
    title = models.CharField(max_length=200, help_text="Short heading, e.g. 'Self-taught Video Editing'")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Experience"
        verbose_name_plural = "Work Experience"

    def __str__(self):
        return self.title


class Project(models.Model):
    """A personal/academic project to showcase in the portfolio."""

    CATEGORY_CHOICES = [
        ('video', 'Video / Reel'),
        ('film', 'Short Film'),
        ('web', 'Web Development'),
        ('game', 'Game Development'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True, help_text="Link to the project, video, or repo")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
