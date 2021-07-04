from django.urls import path
from .views import *
urlpatterns = [

    path("register/", TeamRegisterationView.as_view(), name='team_register'),
    path("list/", TeamListView.as_view(), name='team_list'),
    path('detial/<int:pk>', TeamDetailsView.as_view(), name='team_detial'),
    path('update/<int:pk>/update', TeamUpdateView.as_view(), name='team_update'),
    path('delete/<int:pk>/delete', TeamDeleteView.as_view(), name='team_delete'),
]
