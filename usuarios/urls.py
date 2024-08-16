from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

      path('', views.home_view, name='home'),
    #path('login/', views.login_view, name='login'),
     path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
     path('home/', views.home_view, name='home'),

       path('cursos/', views.curso_list, name='curso_list'),
    path('cursos/nuevo/', views.curso_create, name='curso_create'),
    path('cursos/<int:pk>/editar/', views.curso_update, name='curso_update'),
    path('cursos/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),
      path('about/', views.about_me_view, name='about_me'),
]
