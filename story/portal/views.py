from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages 

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
from portal.forms import BookForm
# Create your views here.

def index(request):
	books = Book.objects.filter(active=True)
	return render(request, 'story_index.html',{'books':books})

#[-----------------------------------]
#|--------     CRUD     -------------|
#[-----------------------------------]
def add_book(request):
	form = BookForm()
	return render(request,'add_book.html',{'form':form})

def create_book(request):
	if request.method =='POST':
		form = BookForm(request.POST)
		if form.is_valid():
			newbook = form.save(commit=False)
			newbook.active = True
			newbook.save()
			return HttpResponseRedirect('/')
		else:
			messages.error(request, "Error")
	else:
		pass

	return HttpResponse()

def update_book(request,book_id):
	book = Book.objects.get(pk=book_id)
	form = BookForm(instance=book)
	return render(request,'update_book.html',{'form':form,'book_id':book_id})

def modify(request,book_id):
	book = Book.objects.get(pk=book_id)
	if request.method == 'POST':
		form = BookForm(request.POST,instance=book)
		if form.is_valid():
			book_form = form.save(commit=False)
			book_form.save()
			return HttpResponseRedirect('/')
		else:
			form = BookForm(instance=book)

	return render(request,'update_book.html',{'form':form,'book_id':book_id})


def delete_book(request,book_id):
	book = Book.objects.get(pk=book_id)
	book.active = False
	book.save()
	return HttpResponseRedirect('/')

#[-----------------------------------]
#|-------  OUTPUT  JSON    ----------|
#[-----------------------------------]
def get_book(request, book_id):
	#pk = stand for primary key , also means unit id
	book = Book.objects.filter(pk=book_id)
	book_info = reconstruct(book)
	response = JsonResponse({'book':book_info})
	return response

def book_json(request):
	books = Book.objects.filter(active=True)
	books_collection = reconstruct(books)

	response = JsonResponse({'books':books_collection})
	return response

# need to recontruct format to output json
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



#[-----------------------------------]
#|--------   UserLogin   ------------|
#[-----------------------------------]
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

