from django.contrib import admin
from django.urls import path
from . import views
from tour.views import TourListView
from tour.views import AgentListView
from tour.views import CustomerListView
from tour.views import TourReviewView
from tour.views import BookingTourView
from tour.views import TourCategoryView


urlpatterns = [
    path('tours/', TourListView.as_view(), name="tour_list"),
    path('tours/review/', TourReviewView.as_view(), name="tour_review"),
    path('tours/booking/', BookingTourView.as_view(), name="booking_tour"),

    # path('tours/<int:pk>/', tour_detail, name="tourDetails"),
    path('agents/', AgentListView.as_view(), name="agent_list"),
    # path('agents/<int:pk>/', agents_detail, name="agentDetail"),
    path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('tours/category/', TourCategoryView.as_view(), name="tour_category"),




]
