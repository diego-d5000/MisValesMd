from django.conf.urls import patterns, include, url
from django.contrib import admin
from contactos import views as c_views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    url(r'^$', c_views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', c_views.LoginView.as_view(), name='login'),
    url(r'^signup/$', c_views.RegisterView.as_view(), name='signup'),
    url(r'^logout/$', c_views.logout, name='logout'),


    url(r'^group/new/$', c_views.newGroup, name='group-new'),
    url(r'^contactos/$', login_required(c_views.PersonView.as_view()), name='get_contactos')

)
