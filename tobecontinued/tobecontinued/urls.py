from django.conf.urls import patterns, include, url
from stories import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^home$', views.homePage),
                       url(r'^submitLine/(?P<storyID>[\d]+)$', views.submitLine),
                       url(r'^story/(?P<storyID>[\d]+)$', views.storyline),
                       url(r'^clear$', views.clear),
                       url(r'^profile$', views.profile),
                       url(r'^create$', views.create),
                       url(r'^createstory$' , views.newStory),
    # Examples:
    # url(r'^$', 'tobecontinued.views.home', name='home'),
    # url(r'^tobecontinued/', include('tobecontinued.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
