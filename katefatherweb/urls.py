from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    re_path(r'^duk1e/', admin.site.urls),
    path('', include('siberian_designs.urls')),
    path('lesson_six/', include('lesson_six.urls')),
    path('reg/', include('register_users.urls')),
]
