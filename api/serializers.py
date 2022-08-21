from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from main.models import User, Cinema, Room, Seat, Movie, ShowTime, Ticket, Feedback


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['image', 'title', 'schedule', 'address', 'contact']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'title']

    # def create(self, validated_data):
    #     create_cinema = validated_data.pop('cinema')
    #     room = Room.objects.create(**validated_data)
    #
    #     for cinema in create_cinema:
    #         Seat.objects.create(room=room, **cinema)
    #
    #     return room


class SeatSerializer(serializers.ModelSerializer):
    # room = RoomSerializer

    class Meta:
        model = Seat
        fields = "__all__"

    # def create(self, validated_data):
    #     create_room = validated_data.pop('room')
    #     seat = Seat.objects.create(**validated_data)
    #
    #     for room in create_room:
    #         Room.objects.create(seat=seat, **room)
    #     return seat


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
