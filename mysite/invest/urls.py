
from django.conf.urls import url

from . import views

app_name = 'invest'

urlpatterns = [
        # ex: /invest/
        url(r'^$', views.index, name='index'),
        url(r'^adddb/$', views.adddb, name='adddb'),
        url(r'^compare/$', views.compare, name='compare'),
        url(r'^data/$', views.dataoperation, name='dataoperation'),
        url(r'^insert/$', views.insert, name='insert'),
        url(r'^delete/$', views.delete, name='delete'),
        url(r'^deleteid/$', views.deleteid, name='deleteid'),
        url(r'^deleteidbatch/$', views.deleteidbatch, name='deleteidbatch'),
        
        # ex: /polls/5/
        #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        # ex: /polls/5/results/
        #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
        # ex: /polls/5/vote/
        #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
            ]
