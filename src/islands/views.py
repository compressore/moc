from core.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Count
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

from django.utils import timezone
import pytz
from functools import wraps

from django.views.decorators.clickjacking import xframe_options_exempt
from core.mocfunctions import *


def index(request):
    list = ReferenceSpace.objects.filter(activated__part_of_project_id=request.project)[:3]
    project = get_object_or_404(Project, pk=request.project)
    context = {
        "show_project_design": True,
        "list": list,
        "dashboard_link": project.slug + ":dashboard",
        "harvesting_link": project.slug + ":hub_harvesting_space",
        "layers": LAYERS,
        "layers_count": LAYERS_COUNT,
        "posts": ForumTopic.objects.filter(part_of_project=request.project).order_by("-last_update__date_created")[:3],
        "news": News.objects.filter(projects=request.project).distinct()[:3]
    }
    return render(request, "islands/index.html", context)

def team(request):
    list = People.objects.filter(parent_list__record_child_id=request.project, parent_list__relationship__id=6)
    context = {
        "list": list,
        "webpage": Webpage.objects.get(pk=31881),
    }
    return render(request, "islands/team.html", context)
