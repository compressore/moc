from django.urls import path
from . import views
from core import views as core
from community import views as community
from library import views as library
from data import views as data
from staf import views as staf
from ie.urls_baseline import baseline_urlpatterns
from ie.urls_staf_baseline import baseline_staf_urlpatterns
from ie.urls_library_baseline import baseline_library_urlpatterns

app_name = "islands"

urlpatterns = baseline_urlpatterns + baseline_library_urlpatterns + baseline_staf_urlpatterns + [

    path("", views.index, name="index"),
    path("team/", views.team, name="team"),
    path("overview/", data.progress, {"style": "grid"}, name="overview"),
    path("news_events/", core.news_events_list, name="news_events"),
    path("about/<slug:slug>/", core.article, { "prefix": "/about/"  }, name="about"),
    path("community/research/projects/", community.projects, name="projects"),
    path("community/research/projects/<int:id>/", community.project, name="project"),
    path("community/research/theses/", library.list, { "type": "island_theses" }),
    path("community/<slug:slug>/", core.article, { "prefix": "/community/"}, name="community"),
    path("resources/map/", library.map, { "article": 59, "tag": 219 }, name="map"),
    path("resources/publications/", library.list, { "type": "islands" }, name="resources"),


    # Controlpanel
    path("controlpanel/organisations/", community.controlpanel_organizations),
    path("controlpanel/organisations/<int:id>/", community.organization_form),
    path("controlpanel/organisations/create/", community.organization_form),

    path("controlpanel/projects/", community.controlpanel_projects),
    path("controlpanel/projects/<int:id>/", community.controlpanel_project_form),
    path("controlpanel/projects/create/", community.controlpanel_project_form),
]
