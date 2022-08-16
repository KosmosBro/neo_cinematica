from django.http import JsonResponse
from rest_framework import viewsets, status, mixins

from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, FeedbackSerializer, TicketSerializer, ShowTimeSerializer, \
    MovieSerializer, SeatSerializer, RoomSerializer, CinemaSerializer
from main.models import User, Feedback, Ticket, ShowTime, Movie, Seat, Room, Cinema


class UserAPIView(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            user = user.filter(title__icontains=title)

        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} User were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get(self, request):
        cinema = Cinema.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            user = cinema.filter(title__icontains=title)

        cinema_serializer = CinemaSerializer(cinema, many=True)
        return JsonResponse(cinema_serializer.data, safe=False)

    def post(self, request):
        cinema = request.data
        serializer = CinemaSerializer(data=cinema)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        count = Cinema.objects.all().delete()
        return JsonResponse({'message': '{} Cinema were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        movie = Movie.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            movie = movie.filter(title__icontains=title)

        movie_serializer = MovieSerializer(movie, many=True)
        return JsonResponse(movie_serializer.data, safe=False)

    def post(self, request):
        movie = request.data
        serializer = MovieSerializer(data=movie)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        count = Movie.objects.all().delete()
        return JsonResponse({'message': '{} Movie were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request):
        room = Room.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            room = room.filter(title__icontains=title)

        room_serializer = RoomSerializer(room, many=True)
        return JsonResponse(room_serializer.data, safe=False)

    def post(self, request):
        room = request.data
        serializer = RoomSerializer(data=room)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        count = Room.objects.all().delete()
        return JsonResponse({'message': '{} Room were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def delete(self, request):
        count = Seat.objects.all().delete()
        return JsonResponse({'message': '{} Seat were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class ShowTimeViewSet(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer

    def delete(self, request):
        count = ShowTime.objects.all().delete()
        return JsonResponse({'message': '{} ShowTime were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class TicketViewSet(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def post(self, request):
        data = request.data

        if Ticket.objects.filter(seat_id=data["seat"], show_time_id=data["show_time"]).exists():
            return JsonResponse({'message': 'This ticket is already booked'})

        else:
            Ticket.objects.create(seat_id=data["seat"], show_time_id=data["show_time"], user=request.user)
            return Response(data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        count = Ticket.objects.all().delete()
        return JsonResponse({'message': '{} Ticket were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self, request):
        feedback = Feedback.objects.all()
        title = request.query_params.get('title', None)
        if title is not None:
            feedback = feedback.filter(title__icontains=title)

        feedback_serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(feedback_serializer.data, safe=False)

    def post(self, request):
        feedback = request.data
        serializer = FeedbackSerializer(data=feedback)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        count = Feedback.objects.all().delete()
        return JsonResponse({'message': '{} Feedback were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
