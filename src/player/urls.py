from django.urls import path
from .views import *
urlpatterns = [
    path("register/", PlayerRegisterationView.as_view(), name='player_register'),
    path("list/", PlayerListView.as_view(), name='player_list'),
    path('detial/<int:pk>', PlayerDetailsView.as_view(), name='player_detial'),
    path('update/<int:pk>/update', PlayerUpdateView.as_view(), name='player_update'),
    path('delete/<int:pk>/delete', PlayerDeleteView.as_view(), name='player_delete'),
]
