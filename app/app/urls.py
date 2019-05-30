from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve


from filesharing import views

urlpatterns = [
    path('',views.home, name='home'),
    path('uploads/form/', views.form_upload, name='form_upload'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
]
