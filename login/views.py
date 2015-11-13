from django.shortcuts import render_to_response, redirect

from django.http import HttpResponse
from django.views.generic import TemplateView,FormView

# Import reverse_lazy method for reversing names to URLs
from django.core.urlresolvers import reverse_lazy

# Import the login_required decorator which can be applied to
# views to enforce that the user should be logged in to access the
# view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login(request):
	return render_to_response('login.html', {})


# This view handles the request to the root URL /. For the mapping,
# check urls.py
def index(request):
  # The current user object is available as request.user. If the
  # user is authenticated, is_authenticated() method of the User
  # object returns True, else it returns False. If the user is logged in
  # redirect to the home page, else to the login page.
  # reverse_lazy() method takes a URL pattern name and returns the URL path.
  # Here it is used to get the URL paths of home and login pages.

  if request.user.is_authenticated():
    return redirect(reverse_lazy('home'))
  else:
    return redirect(reverse_lazy('login'))
  
# login_required decorator, when applied to a view enforces the rule that
# a user has to be logged in to the access the view. If he is not logged in,
# he is redirected to the login page.
@login_required
def home(request):
	return render_to_response('index.html', {'username':request.user.username})