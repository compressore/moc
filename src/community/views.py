from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from core.models import *
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
import pytz

PROJECT_ID = settings.PROJECT_ID_LIST
RELATIONSHIP_ID = settings.RELATIONSHIP_ID_LIST

# Quick function to make someone the author of something
def set_autor(author, item):
    RecordRelationship.objects.create(
        relationship_id = RELATIONSHIP_ID["author"],
        record_parent_id = author,
        record_child_id = item,
    )

def index(request):

    context = {
        "show_project_design": True,
    }

    return render(request, "template/blank.html", context)

def person(request, id):
    article = get_object_or_404(Webpage, pk=PAGE_ID["people"])
    info = get_object_or_404(People, pk=id)
    context = {
        "edit_link": "/admin/core/people/" + str(info.id) + "/change/",
        "info": info,
    }
    return render(request, "person.html", context)

def people_list(request):
    info = get_object_or_404(Webpage, pk=PAGE_ID["people"])
    context = {
        "edit_link": "/admin/core/article/" + str(info.id) + "/change/",
        "info": info,
        "list": People.objects.all(),
    }
    return render(request, "people.list.html", context)


def projects(request):

    if "import" in request.GET:
        import csv
        print("importing")
        file = settings.MEDIA_ROOT + "/import/projects.csv"
        funders = {}
        with open(file, "r") as csvfile:
            contents = csv.DictReader(csvfile)
            for row in contents:
                meta = {}
                name = row["name"]
                print(name)
                check = PublicProject.objects.filter(name=name)
                if check:
                    info = check[0]
                    info.description = row["description"]
                    if row["start_date"]:
                        info.start_date = row["start_date"]
                    if row["end_date"]:
                        info.end_date = row["end_date"]
                    if row["logo"] and not info.image:
                        info.image = row["logo"]

                    if row["funding_program"]:
                        funder = row["funding_program"]
                        if funder in funders:
                            funder_id = funders[funder]
                        else:
                            checkfunder = Organization.objects.filter(name=funder)
                            if checkfunder:
                                f = checkfunder[0]
                            else:
                                f = Organization.objects.create(
                                    type = "funding_program",
                                    name = funder,
                                )
                            funder_id = f.id
                            funders[funder] = f.id

                        try:
                            RecordRelationship.objects.create(
                                relationship_id = 5,
                                record_parent_id = funder_id,
                                record_child = info,
                            )
                        except:
                            print("Error!")

                    if row["budget"]:
                        meta["budget"] = row["budget"]
                        meta["budget_currency"] = "EUR"
                    if row["institution"]:
                        meta["institution"] = row["institution"]
                    info.meta_data = meta
                    info.save()



    list = PublicProject.objects.all()
    context = {
        "list": list,
        "header_title": "Projects",
        "header_subtitle": "Research and intervention projects that are happening all over the world.",
    }
    return render(request, "community/projects.html", context)

def project(request, id):
    info = PublicProject.objects.get(pk=id)
    context = {
        "info": info,
        "header_title": info.name,
        "header_subtitle": "Projects",
        "edit_link": "/admin/core/publicproject/" + str(info.id) + "/change/",
        "show_relationship": info.id,
        "relationships": info.child_list.all(),
    }
    return render(request, "community/project.html", context)

def organizations(request, slug=None):
    list = Organization.objects.filter(type=slug)
    context = {
        "list": list,
        "load_datatables": True,
        "slug": slug,
        "header_title": slug,
        "header_subtitle": "List of organisations active in the field of urban metabolism",
    }
    return render(request, "community/organizations.html", context)

def organization(request, slug, id):
    info = get_object_or_404(Organization, pk=id)
    context = {
        "info": info,
        "header_title": info.name,
        "header_subtitle": info.get_type_display,
        "edit_link": "/admin/core/organization/" + str(info.id) + "/change/",
    }
    return render(request, "community/organization.html", context)

# FORUM

def forum_list(request):
    list = Message.objects.filter(parent__isnull=True)
    context = {
        "list": list,
    }
    return render(request, "forum.list.html", context)

def forum(request, id, project_name=None):
    info = get_object_or_404(Record, pk=id)
    list = Message.objects.filter(Q(parent=id) | Q(id=id))
    context = {
        "info": info,
        "list_messages": list,
        "load_messaging": True,
        "forum_title": info.name,
    }
    if request.method == "POST":

        message = Message.objects.create(
            name = "Reply to: " + info.name,
            description = request.POST.get("text"),
            parent = info,
        )
        set_autor(request.user.people.id, message.id)

        if hasattr(info, "forumtopic"):
            info.forumtopic.last_update = timezone.now()
            info.forumtopic.save()

        if request.FILES:
            files = request.FILES.getlist("file")
            for file in files:
                info_document = Document()
                info_document.file = file
                info_document.save()
                new.attachments.add(info_document)
        messages.success(request, "Your message has been posted.")

        if "return" in request.POST:
            return redirect(request.POST["return"])
    return render(request, "forum.topic.html", context)

def forum_form(request, id=False, project_name=None):

    project = None
    if project_name:
        project = get_object_or_404(Project, pk=PROJECT_ID[project_name])

    if request.method == "POST":
        info = ForumTopic.objects.create(
            part_of_project = project,
            name = request.POST.get("title"),
            last_update = timezone.now(),
        )
        set_autor(request.user.people.id, info.id)
        message = Message.objects.create(
            name = request.POST.get("title"),
            description = request.POST.get("text"),
            parent = info,
        )
        set_autor(request.user.people.id, message.id)

        if request.FILES:
            files = request.FILES.getlist("file")
            for file in files:
                info_document = Document()
                info_document.file = file
                info_document.save()
                message.attachments.add(info_document)
        messages.success(request, "Your message has been posted.")

        if project_name == "ascus":
            return redirect(project_name + ":forum", info.id)

        return redirect(message.get_absolute_url())

    context = {
        "load_messaging": True,
    }
    return render(request, "forum.form.html", context)

