from django.urls import path

from webapp.views import index_view, game_view

urlpatterns = [
    path('', index_view),
    path('game/', game_view)
]
