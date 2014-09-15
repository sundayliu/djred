from django.conf.urls import url,patterns
from tango.views import index

urlpatterns = patterns('',
                       url(r'^$',index,name="index"),
                       )