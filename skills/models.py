from django.db import models


class Skill(models.Model):
    """A creative/technical skill with a star rating out of 5."""

    CATEGORY_CHOICES = [
        ('creative', 'Creative'),
        ('technical', 'Technical'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='creative')
    rating = models.PositiveSmallIntegerField(default=5, help_text="Rating out of 5 stars")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"


class Software(models.Model):
    """A software/tool the person uses, with a status note (e.g. In Progress)."""
    name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5, help_text="Proficiency out of 5 stars")
    status_note = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. 'In Progress', 'About to start'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Software"
        verbose_name_plural = "Software"

    def __str__(self):
        return self.name
