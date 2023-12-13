from django.contrib import admin
from django.urls import path
from . import views
from tour.views import TourListView
# from tour.views import AgentListView
from tour.views import TourReviewListView
from tour.views import TourReviewDetailView
from tour.views import BookingTourListView
from tour.views import TourCategoryView
from tour.views import TourCategoryDetailView
from tour.views import AgentDetailView
from tour.views import AgentListView
from tour.views import BookingTourDetailView
from tour.views import TourDetailView


urlpatterns = [
    path('tours/', TourListView.as_view(), name="tour_list"),
    path('tours/details/<int:pk>/', TourDetailView.as_view(), name="tour_detail"),
    path('tours/review/<int:pk>/', TourReviewDetailView.as_view(),
         name='tour_review_detail'),

    path('tours/reviews/', TourReviewListView.as_view(), name='tourreview_list'),
    path('tours/booking/', BookingTourListView.as_view(), name="booking_tour"),
    path('tours/booking/<int:pk>/',
         BookingTourDetailView.as_view(), name='booking_detail'),


    # path('tours/<int:pk>/', tour_detail, name="tourDetails"),
    path('agents/list/', AgentListView.as_view(), name="agent_list"),

    path('agents/details/<int:pk>/',
         AgentDetailView.as_view(), name='agent_detail'),



    # path('agents/<int:pk>/', agents_detail, name="agentDetail"),
    #     path('customers/', CustomerListView.as_view(), name="customer_list"),
    path('tours/category/', TourCategoryView.as_view(), name="tour_category"),
    path('tours/category/<int:pk>/', TourCategoryDetailView.as_view(),
         name='tour_category_detail'),




]
