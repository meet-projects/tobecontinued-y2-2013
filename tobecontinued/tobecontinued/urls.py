from django.conf.urls import patterns, include, url
from stories import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^home$', views.homePage),
                       url(r'^story/(?P<storyID>\d+)/submitLine$', views.submitLine, name='submitLine'),
                       url(r'^story/(?P<storyID>\d+)$', views.storyline),
                       url(r'^create$', views.create),
                       url(r'^newStory$' , views.newStory),
                       url(r'^signup$',views.signup),
                       
                      
    # Examples:
    # url(r'^$', 'tobecontinued.views.home', name='home'),
    # url(r'^tobecontinued/', include('tobecontinued.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
