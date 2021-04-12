from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('all-hoods/', views.neighborhoods, name='neighborhoods'),
    path('join_hood/<int:id>/', views.join_neighborhood, name='join-hood'),
    path('leave_hood/<int:id>/', views.leave_neighborhood, name='leave-hood'), 
    path('single_hood/<int:hood_id>/', views.single_neighborhood, name='single-hood'),
    path('<int:hood_id>/post/', views.create_post, name='post'),
    path('search/', views.search_business, name='search')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)