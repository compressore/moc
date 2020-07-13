""" 
Baseline URLs which we want to apply to every site that 
works with STAF data.
We import this file in every urls file so if we ever have
to change anything, we can do it in one place
"""

from django.urls import include, path
from staf import views as staf
from library import views as library
from core import views as core
from data import views as data

#
# Baseline links shared between all projects
# Last change Jul 8, 2020
#

baseline_staf_urlpatterns = [

    path("layers/worksheet/", staf.layers_worksheet, name="data_layers_worksheet"),
    path("dashboards/<slug:slug>/controlpanel/worksheet/", staf.referencespace_worksheet, name="referencespace_worksheet"),
    path("dashboards/<slug:slug>/controlpanel/worksheet/<int:tag>/", staf.referencespace_worksheet_tag),
    path("dashboards/<slug:space>/controlpanel/worksheet/<int:tag>/form/", library.form),

    # Controlpanel
    path("dashboards/<slug:space>/controlpanel/", core.controlpanel, name="controlpanel_space"),
    path("dashboards/<slug:space>/controlpanel/data-articles/", core.controlpanel_data_articles, name="controlpanel_data_articles"),
    path("dashboards/<slug:space>/controlpanel/data-articles/create/", core.controlpanel_data_article, name="controlpanel_data_article"),
    path("dashboards/<slug:space>/controlpanel/data-articles/<int:id>/", core.controlpanel_data_article, name="controlpanel_data_article"),

    path("resources/publications/", library.list, { "type": "islands" }, name="library"),
    path("resources/publications/<int:id>/", library.item, { "show_export": False }, name="library_item"),

    # Data dashboards
    path("dashboards/<slug:space>/sectors/", data.sectors, name="sectors"),
    path("dashboards/<slug:space>/sectors/<slug:sector>/", data.sector, name="sector"),
    path("dashboards/<slug:space>/sectors/<slug:sector>/<slug:article>/", data.article, name="article"),
    path("dashboards/<slug:space>/datasets/", data.datasets, name="datasets"),
    path("dashboards/<slug:space>/datasets/<slug:dataset>/", data.dataset, name="dataset"),
    path("dashboards/<slug:space>/resources/photos/", data.photos, name="photos"),
    path("dashboards/<slug:space>/resources/reports/", data.library, {"type": "reports"}, name="reports"),
    path("dashboards/<slug:space>/resources/theses/", data.library, {"type": "theses"}, name="theses"),
    path("dashboards/<slug:space>/resources/journal-articles/", data.library, {"type": "articles"}, name="journal_articles"),
    path("dashboards/<slug:space>/maps/", data.maps, name="maps"),
    path("dashboards/<slug:space>/", data.dashboard, name="dashboard"),
]