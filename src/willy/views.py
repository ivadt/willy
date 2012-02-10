from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from willy.forms import RegistrationForm
from willy.gallery.models import Category

def welcome(request):
    categories = Category.objects.filter(owner=request.user)

    return render_to_response('welcome.html',
                              {'user' : request.user,
                               'categories' : categories},
                              context_instance=RequestContext(request))

def register(request):
    if request.method == 'GET':
        return render_to_response('register.html',
                                  {'form' : RegistrationForm()},
                                  context_instance=RequestContext(request))

    form = RegistrationForm(request.POST)
    if form.is_valid():
        user_data = {}
        user_data['username'] = form.cleaned_data['username']
        user_data['password'] = form.cleaned_data['password1']
        user_data['email'] = form.cleaned_data['email']
        user = User.objects.create_user(**user_data)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        # Create a new category with the same name as the username
        category = Category(name=user.username, owner=user)
        category.category_parent = category.id
        category.save()

        user = authenticate(username=user_data['username'], password=user_data['password'])
        login(request, user)
        return redirect('/welcome/')

    return render_to_response('register.html',
                              {'form' : form},
                              context_instance=RequestContext(request))
