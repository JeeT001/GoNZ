from django.contrib import admin
from django.urls import path
from . import views
from tour.views import TourListView
from tour.views import AgentListView


urlpatterns = [
    path('tours/', TourListView.as_view(), name="tour_list"),
    # path('tours/', tour_list, name="tourList"),
    # path('tours/<int:pk>/', tour_detail, name="tourDetails"),
    path('agents/', AgentListView.as_view(), name="agent_list"),
    # path('agents/<int:pk>/', agents_detail, name="agentDetail"),

]
