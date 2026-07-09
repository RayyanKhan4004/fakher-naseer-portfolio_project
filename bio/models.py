from django.db import models


class Bio(models.Model):
    """Stores the main profile / bio information shown on the homepage."""
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200, help_text="e.g. Video - Photographer and Editor")
    profile_picture = models.ImageField(upload_to='profile/')
    description = models.TextField(help_text="Objective / About Me paragraph")
    email = models.EmailField(blank=True, null=True)
    phone_primary = models.CharField(max_length=20, blank=True, null=True)
    phone_secondary = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True, help_text="Facebook username/handle")
    instagram = models.CharField(max_length=150, blank=True, null=True, help_text="Instagram username/handle")
    github = models.CharField(max_length=150, blank=True, null=True, help_text="GitHub username")
    work_drive_link = models.URLField(blank=True, null=True, help_text="Link to portfolio work / drive folder")

    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bio"

    def __str__(self):
        return self.name
