from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from typing import Optional
from django.views.generic import DetailView
from django.views.generic import ListView


from .models import Agents, Tours, TourReview, Customer, BookingTour, TourCategory


class TourListView(ListView):
    model = Tours
    template_name = 'tours/tour_list.html'
    context_object_name = 'tours'


class TourReviewListView(ListView):
    model = TourReview
    template_name = 'tours/tour_review.html'
    context_object_name = 'reviews'


class TourReviewDetailView(DetailView):
    model = TourReview
    template_name = 'tours/tour_review_detail.html'
    context_object_name = 'review'


class BookingTourListView(ListView):
    model = BookingTour
    template_name = 'tours/booking_tour.html'
    context_object_name = 'bookings'


class BookingTourDetailView(DetailView):
    model = BookingTour
    template_name = 'tours/booking_detail.html'
    context_object_name = 'booking'


# class AgentListView(generic.ListView):
#     model = Agents
#     template_name = 'tours/agent_list.html'

class AgentListView(ListView):
    model = Agents
    # Set the template name as per your project structure
    template_name = 'tours/agent_list.html'
    context_object_name = 'agentss'


class AgentDetailView(DetailView):
    model = Agents
    # Set the template name as per your project structure
    template_name = 'tours/agent_detail.html'
    context_object_name = 'agent'


class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'tours/customer_list.html'


class TourCategoryView(generic.ListView):
    model = TourCategory
    template_name = 'tours/tour_category.html'
    context_object_name = 'categories'


class TourCategoryDetailView(DetailView):
    model = TourCategory
    template_name = 'tours/tours_category_detail.html'
    context_object_name = 'category'


class TourDetailView(DetailView):
    model = Tours
    template_name = 'tours/tour_detail.html'
    context_object_name = 'tours'
