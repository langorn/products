from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect


# from crm.forms import UserForm, UserProfileForm
from django.db.models import Q
from django.core import serializers
import json

from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.utils.functional import Promise
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from portal.models import Book
# Create your views here.

def index(request):
	books = Book.objects.filter(active=True)
	return render(request, 'story_index.html',{'books':books})

def book_json(request):
	books = Book.objects.filter(active=True)
	books_collection = reconstruct(books)

	response = JsonResponse({'books':books_collection})
	return response

# need to recontruct format to ouput json
def reconstruct(items):
	items_collections = []
	for item in items:
		newbook = {
			'id':item.id,		
			'name': item.name,
			'author':item.author,
			'last_update':item.last_update
		}
	items_collections.append(newbook)
	return items_collections

#user login
def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                print 'user is active'
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("/login_fail")
        else:
            #print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'login.html', {}, context)

