from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('character_select/<username>/', views.charSel, name='character_select'),
    path('character_creation/', views.CharCreation.as_view(), name='character_create'),
    path('<charname>/', views.charInfo, name="character_info"),
    path('<charname>/monster_list/', views.monsters, name="monster_list"),
    path('<charname>/battle/<monstername>/', views.battle, name="battle"),
    path('<charname>/inventory/', views.inventory, name="inventory"),
    path('<charname>/delete', views.CharacterDelete, name="character_delete")
]