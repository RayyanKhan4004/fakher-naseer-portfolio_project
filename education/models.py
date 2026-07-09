from django.db import models


class Education(models.Model):
    """A single academic qualification entry."""
    degree_title = models.CharField(max_length=200, help_text="e.g. Bachelor in Computer Science")
    institution = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. UMT")
    duration = models.CharField(max_length=100, help_text="e.g. 2023 - 2027 or In Progress")
    score = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. 1096/1100 or CGPA 3.29")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first")

    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Education"
        verbose_name_plural = "Education Entries"

    def __str__(self):
        return self.degree_title
