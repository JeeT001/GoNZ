from django.contrib import admin

from tour.models import Agents, Tours, TourReview, Customer, BookingTour, TourCategory

# Register your models here.
admin.site.register(Agents)
admin.site.register(Tours)
admin.site.register(TourReview)
admin.site.register(Customer)
admin.site.register(BookingTour)
admin.site.register(TourCategory)
