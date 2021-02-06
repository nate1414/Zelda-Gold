from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('game', views.game),
    path('gold', views.gold),
    path('reset', views.reset),
    path('game/edit/<int:id>', views.edit_profile),
    path('game/edit/<int:id>/update', views.update),
    path('delete_user', views.delete_user),
    path('you_won', views.you_won),
    path('you_lost', views.you_lost),
]