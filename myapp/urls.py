from django.http import HttpResponse
from django.conf.urls import patterns, url

def hello_world(request):
    return HttpResponse('Hello world')

urlpatterns = patterns('',
    url(r'^$', hello_world),
)
