from django.contrib import admin
from django.urls import path
from . import views
from tour.views import TourListView

urlpatterns = [
    path('tours/', TourListView.as_view(), name="tour_list"),
    # path('tours/', tour_list, name="tourList"),
    # path('tours/<int:pk>/', tour_detail, name="tourDetails"),
    # path('agents/', agents_list, name="agentList"),
    # path('agents/<int:pk>/', agents_detail, name="agentDetail"),

]
