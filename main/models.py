from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Cinema(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=50)
    schedule = models.CharField(max_length=200, verbose_name='расписание')
    address = models.CharField(max_length=200, verbose_name='адрес')
    contact = models.CharField(max_length=200, verbose_name='контакты')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['id', 'title']


class Room(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seat', null=True)
    number_row = models.CharField(max_length=10)
    number_seat = models.CharField(max_length=10)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', null=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    price = models.IntegerField()


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show_time = models.ForeignKey(ShowTime, on_delete=models.CASCADE)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user')
    comment = models.CharField(max_length=500)
    creation_date = models.DateTimeField(default=timezone.now)
