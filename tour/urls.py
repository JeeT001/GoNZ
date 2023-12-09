from django.contrib import admin
from django.urls import path
from . import views
from tour.views import TourListView
# from tour.views import AgentListView
from tour.views import CustomerListView
from tour.views import TourReviewView
from tour.views import BookingTourListView
from tour.views import TourCategoryView
from tour.views import AgentDetailView
from tour.views import AgentListView
from tour.views import BookingTourDetailView


urlpatterns = [
    path('tours/', TourListView.as_view(), name="tour_list"),
    path('tours/review/', TourReviewView.as_view(), name="tour_review"),
    path('tours/booking/', BookingTourListView.as_view(), name="booking_tour"),
    path('tours/booking/<int:pk>/',
         BookingTourDetailView.as_view(), name='booking_detail'),


    # path('tours/<int:pk>/', tour_detail, name="tourDetails"),
    path('agents/list/', AgentListView.as_view(), name="agent_list"),

    path('agents/details/<int:pk>/',
         AgentDetailView.as_view(), name='agent_detail'),



    # path('agents/<int:pk>/', agents_detail, name="agentDetail"),
    path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('tours/category/', TourCategoryView.as_view(), name="tour_category"),




]
