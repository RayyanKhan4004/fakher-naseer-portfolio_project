from django.shortcuts import render
from .models import Bio
from education.models import Education
from skills.models import Skill, Software
from experience.models import Experience, Project


def home(request):
    context = {
        'bio': Bio.objects.first(),
        'education_list': Education.objects.all(),
        'creative_skills': Skill.objects.filter(category='creative'),
        'technical_skills': Skill.objects.filter(category='technical'),
        'software_list': Software.objects.all(),
        'experience_list': Experience.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'bio/home.html', context)
