from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main_reg'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('logout', views.LogoutFormView.as_view(), name ='logout'),
    path('login', views.LoginFormView.as_view(), name='login'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
