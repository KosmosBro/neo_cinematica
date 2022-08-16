from django.contrib import admin

# Register your models here.

from main.models import Ticket, ShowTime, Seat, Room, Cinema,Feedback, Movie

admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(ShowTime)
admin.site.register(Ticket)
admin.site.register(Feedback)
admin.site.register(Movie)
