from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^preguntas/nueva', 'autoEvaluacion.views.newPregunta', name='nueva_pregunta'),
	url(r'^asignaturas/nueva', 'autoEvaluacion.views.newAsignatura', name='nueva_asignatura'),
	url(r'^Examenes/nuevo', 'autoEvaluacion.views.newExamen', name='nuevo_examen'),
  	url(r'^admin/', include(admin.site.urls)),

	
	url(r'^$', 'login.views.index'),
      
	# Map the 'app.hello.home' view to the URL /home/ and name the pattern as 'home'.
	url(r'^home/$', 'login.views.home', name='home'),

	# Map the 'django.contrib.auth.views.login' view to the /login/ URL.
	# The additional parameters to the view are passed via the 3rd argument which is
	# a dictionary of various parameters like the name of the template to be
	# used by the view.
	url(r'^login/$', 'django.contrib.auth.views.login',
	  {
	   "template_name" : "login.html",
	  },
	  name="login"),
	  
	# Map the 'django.contrib.auth.views.logout' view to the /logout/ URL.
	# Pass additional parameters to the view like the page to show after logout
	# via a dictionary used as the 3rd argument.
	url(r'^logout/$', 'django.contrib.auth.views.logout',
	  {
	    "next_page" : reverse_lazy('login')
	  }, name="logout"),

	

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)