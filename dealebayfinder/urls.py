from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('login/',LoginView.as_view(template_name='dealebayfinder/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='dealebayfinder/logout.html'), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
