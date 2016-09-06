"""story URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #index 
    url(r'^$','portal.views.index', name='index'),

    #fb_bot
    url(r'^fb_bot/', include('fb_bot.urls')),

    #output_ json
    url(r'books/','portal.views.book_json', name='books'),
    url(r'book/(?P<book_id>\d+)/$','portal.views.get_book', name='get_book'),

    #CRUD
    url(r'book/add/$','portal.views.add_book', name='add_book'),
    url(r'book/create/','portal.views.create_book', name='create_book'),
    url(r'book/update/(?P<book_id>\d+)/','portal.views.update_book', name='update_book'),
    url(r'book/modify/(?P<book_id>\d+)/','portal.views.modify', name='modify'),
    url(r'book/delete/(?P<book_id>\d+)/','portal.views.delete_book', name='delete_book'),
    
    #user
    url(r'^login/','portal.views.user_login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/'} ,name='logout')
]
