"""csoorhimzes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('kapcsolat/', views.kapcsolat, name="contact"),
    path('rolunk/', views.rolunk, name="rolunk"),
    path('viszonteladoknak/', views.viszonteladoknak, name="viszonteladoknak"),
    path('cegeknek/', views.cegeknek, name="cegeknek"),


    path('kategoria/<int:category_id>-<slug:category_slug>', views.kategoriak, name='kategoriak'),
    path('termekek/<int:category_id>-<slug:category_slug>', views.termekek, name='product'),



    path('summernote/', include('django_summernote.urls')),
    path('kereses/', views.kereses, name='kereses'),
    path('blog/', views.blog, name='blog'),
    path('<int:category_id>-<slug:category_slug>/<int:product_id>-<slug:product_slug>', views.oneProduct, name="oneProduct")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
