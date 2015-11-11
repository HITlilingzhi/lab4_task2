from django.conf.urls import *
from lab3.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^new_book/$', new_book),
    (r'^book_list/$', book_list),
    (r'^search_author/$', search_author),
    (r'^new_author/$', new_author),
    (r'^author_list/$', author_list),
    (r'^delete_book/$', delete_book),
    (r'^update_book/$', update_book),
    (r'^show_book_information/$', show_book_information),
    (r'^delete_author/$', delete_author),
    ('^$',book_list),
    
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
