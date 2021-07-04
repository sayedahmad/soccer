from django.urls import path
from .views import *
urlpatterns = [

    path("register/", MatchRegisterationView.as_view(), name='match_register'),
    path("list/", MatchListView.as_view(), name='match_list'),
    path('detial/<int:pk>', MatchDetailsView.as_view(), name='match_detial'),
    path('update/<int:pk>/update', MatchUpdateView.as_view(), name='match_update'),
    path('delete/<int:pk>/delete', MatchDeleteView.as_view(), name='match_delete'),
    path('matchplayer/', MatchMakerView.as_view(), name='match_player'),
]
