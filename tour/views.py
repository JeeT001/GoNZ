from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from typing import Optional


from .models import Agents, Tours, TourReview, Customer, BookingTour, TourCategory


class TourListView(generic.ListView):
    model = Tours
    template_name = 'tours/tour_list.html'


class TourReviewView(generic.ListView):
    model = TourReview
    template_name = 'tours/tour_review.html'


class BookingTourView(generic.ListView):
    model = BookingTour
    template_name = 'tours/booking_tour.html'


class AgentListView(generic.ListView):
    model = Agents
    template_name = 'tours/agent_list.html'


class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'tours/customer_list.html'
