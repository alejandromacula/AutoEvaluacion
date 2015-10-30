from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'autoEvaluacion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^preguntas/nueva', 'autoEvaluacion.views.newPregunta', name='nueva_pregunta'),
	url(r'^asignaturas/nueva', 'autoEvaluacion.views.newAsignatura', name='nueva_asignatura'),
	url(r'^Examenes/nuevo', 'autoEvaluacion.views.newExamen', name='nuevo_examen'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/', 'autoEvaluacion.views.login', name='login'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
