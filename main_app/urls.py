from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('character_select/<username>/', views.charSel, name='character_select'),
    path('character_creation/', views.CharCreation.as_view(), name='character_create')

]