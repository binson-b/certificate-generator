from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView #import list_detail

from announcements.models import Announcement
from announcements.views import *


announcement_detail_info = {
    "queryset": Announcement.objects.all(),
}

print announcement_detail_info
urlpatterns = patterns("",
    url(r"^(?P<object_id>\d+)/$", ListView.as_view(),
    	name="announcement_detail"),
    url(r"^(?P<object_id>\d+)/hide/$", announcement_hide,
        name="announcement_hide"),
    url(r"^a", announcement_list, name="announcement_home"),
)
