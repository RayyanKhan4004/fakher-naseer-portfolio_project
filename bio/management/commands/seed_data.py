import os
from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

from bio.models import Bio
from education.models import Education
from skills.models import Skill, Software
from experience.models import Experience, Project


class Command(BaseCommand):
    help = "Seeds the database with the portfolio owner's data and creates the admin superuser."

    def handle(self, *args, **options):

        # 1. Admin superuser --------------------------------------------------
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin', email='', password='admin@')
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created."))
        else:
            self.stdout.write("Superuser 'admin' already exists, skipping.")

        # 2. Bio ---------------------------------------------------------------
        if not Bio.objects.exists():
            bio = Bio(
                name="Fakhar Naseer",
                job_title="Video - Photographer and Editor",
                description=(
                    "I aspire to become a professional filmmaker and also an actor, to fulfill my dreams. "
                    "Initially, I want to learn the fundamentals of all aspects of videography and, "
                    "In sha Allah, eventually step into the industry. For now, I am applying here to test "
                    "and improve my skills."
                ),
                email="fakharnaseer38@gmail.com",
                phone_primary="+92 349 3983951",
                phone_secondary="+92 339 3983951",
                facebook="fakhar.naseer38",
                instagram="fakhar.naseer",
                github="fakharnaseer",
                work_drive_link="",
            )
            profile_pic_path = settings.MEDIA_ROOT / 'profile' / 'fakhar_profile.jpg'
            if os.path.exists(profile_pic_path):
                with open(profile_pic_path, 'rb') as f:
                    bio.profile_picture.save('fakhar_profile.jpg', File(f), save=False)
            bio.save()
            self.stdout.write(self.style.SUCCESS("Bio created."))
        else:
            self.stdout.write("Bio already exists, skipping.")

        # 3. Education -----------------------------------------------------
        if not Education.objects.exists():
            Education.objects.bulk_create([
                Education(
                    degree_title="Bachelor in Computer Science",
                    institution="University of Management and Technology (UMT)",
                    duration="2023 - 2027 (In Progress)",
                    score="Current CGPA 3.29",
                    order=1,
                ),
                Education(
                    degree_title="Intermediate (ICS)",
                    institution="",
                    duration="2021 - 2023",
                    score="903 / 1100",
                    order=2,
                ),
                Education(
                    degree_title="Matric with Computer Science",
                    institution="",
                    duration="2019 - 2021",
                    score="1096 / 1100",
                    order=3,
                ),
            ])
            self.stdout.write(self.style.SUCCESS("Education entries created."))
        else:
            self.stdout.write("Education entries already exist, skipping.")

        # 4. Skills & Software ------------------------------------------------
        if not Skill.objects.exists():
            Skill.objects.bulk_create([
                Skill(name="Videography", category='creative', rating=5, order=1),
                Skill(name="Photography", category='creative', rating=5, order=2),
                Skill(name="Video Editing", category='creative', rating=5, order=3),
                Skill(name="Creative Ideas", category='creative', rating=5, order=4),
                Skill(name="Vlogging", category='creative', rating=5, order=5),
                Skill(name="Python", category='technical', rating=4, order=6),
                Skill(name="Django", category='technical', rating=4, order=7),
                Skill(name="C++", category='technical', rating=4, order=8),
                Skill(name="C#", category='technical', rating=3, order=9),
                Skill(name="JavaScript", category='technical', rating=3, order=10),
                Skill(name="HTML & CSS", category='technical', rating=4, order=11),
            ])
            self.stdout.write(self.style.SUCCESS("Skills created."))
        else:
            self.stdout.write("Skills already exist, skipping.")

        if not Software.objects.exists():
            Software.objects.bulk_create([
                Software(name="CapCut", rating=5, status_note="Proficient", order=1),
                Software(name="DaVinci Resolve", rating=4, status_note="In Progress", order=2),
                Software(name="Blender", rating=1, status_note="About to Start", order=3),
            ])
            self.stdout.write(self.style.SUCCESS("Software entries created."))
        else:
            self.stdout.write("Software entries already exist, skipping.")

        # 5. Work Experience ---------------------------------------------------
        if not Experience.objects.exists():
            Experience.objects.bulk_create([
                Experience(
                    title="Self-Taught Video Editor",
                    description="Been trying to edit videos from a really young age, learning the craft independently.",
                    order=1,
                ),
                Experience(
                    title="Short Film & VFX Work",
                    description="Made a short film, and also a lot of VFX related reels for fun.",
                    order=2,
                ),
                Experience(
                    title="University Video Assignments",
                    description="Handled all the video related assignments and tasks in university.",
                    order=3,
                ),
                Experience(
                    title="Vlogging",
                    description=(
                        "Used to make vlogs regularly; the Instagram account is currently deactivated "
                        "and will be reactivated soon."
                    ),
                    order=4,
                ),
            ])
            self.stdout.write(self.style.SUCCESS("Experience entries created."))
        else:
            self.stdout.write("Experience entries already exist, skipping.")

        # 6. Projects ------------------------------------------------------
        if not Project.objects.exists():
            Project.objects.bulk_create([
                Project(
                    title="E-Shopping Website",
                    category="web",
                    description="A personal e-commerce / online shopping website project.",
                    order=1,
                ),
                Project(
                    title="Short Film",
                    category="film",
                    description="An independently made short film, shot and edited from scratch.",
                    order=2,
                ),
                Project(
                    title="Creative Reels & VFX Edits",
                    category="video",
                    description="A collection of VFX-based reels and creative video edits made for fun and practice.",
                    order=3,
                ),
                Project(
                    title="Zombie Survival Game (Unity)",
                    category="game",
                    description="A zombie-themed survival game built using the Unity game engine.",
                    order=4,
                ),
            ])
            self.stdout.write(self.style.SUCCESS("Project entries created."))
        else:
            self.stdout.write("Project entries already exist, skipping.")

        self.stdout.write(self.style.SUCCESS("Database seeding complete."))
