from django.conf.urls import include, url

from .views import *

urlpatterns = [
    url(r'^disp$', disp),
    url(r'^job$', job),
    url(r'^process$', job_process),
    url(r'^behind$', job_behind),
]