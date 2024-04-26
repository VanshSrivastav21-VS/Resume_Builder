from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name = 'resume'),
    path("resumetemplate", views.resumetemplate, name="resumetemplate"),
    path("resume_templates", views.resume_templates, name="resume_templates"),
    path("resumetemplatedownload", views.resumetemplatedownload, name="resumetemplatedownload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)