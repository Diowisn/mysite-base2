from django.contrib import admin
from django.urls import path, include
from posting.views import * 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('kebijakanprivasi/', kebijkanprivasi, name='kebijakan privasi'),
    
    path('api/', include('posting.urls')),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    

]

urlpatterns += staticfiles_urlpatterns()

