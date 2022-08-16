from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from main.models import Cinema, Room, Movie, Seat, ShowTime, Feedback, Ticket


class TestUserApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos@mail.ru', password='1234')

    def test_user_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/user/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_user_add_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/user/'

        data = {
            'username': 'kos',
            'first_name': 'Turan',
            'last_name': 'Kosmos',
            "email": "kosmosbro@mail.ru",
            'password': "1234",

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_user_delete_api(self):
        self.client.login(username='kos', password='1234')

        url = '/api/user/'

        data = {
            'username': 'kos',
            'first_name': 'Turan',
            'last_name': 'Kosmos',
            'password': "1234",

        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_user_api_fail(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/user/'

        data = {
            'email': 12,
            'first_name': 'Turanss',
            'last_name': 'Kosmosss',
            'password': "1234",

        }

        with self.assertRaises(TypeError):
            User.objects.create(data, url)


class TestCinemaApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos@mail.ru', password='1234')

    def test_cinema_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/cinema/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_cinema_add_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/cinema/'

        data = {
            'title': 'Ala-Too',
            'schedule': '21212121',
            'address': 'bishkek',
            'contact': "1234",

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_cinema_update_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/cinema/'

        data = {
            'title': 'Ala-Too',
            'schedule': '21assas212121',
            'address': 'bishkek',
            'contact': "1234",

        }

        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_cinema_delete_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/cinema/'

        data = {
            'title': 'Ala-Too',
            'schedule': '21assas212121',
            'address': 'bishkek',
            'contact': "1234",

        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_cinema_api_fail(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/cinema/'

        data = {
            'tite': 'Ala-Too',
            'schedule': '21assas212121' * 200,
            'address': 'bishkek',
            'contact': "1234",

        }
        with self.assertRaises(TypeError):
            Cinema.objects.create(data, url)


class TestRoomApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos@mail.ru', password='1234')
        cls.cinema = Cinema.objects.create(id=2, title='Ala_too', schedule='12121221', address='bishkek',
                                           contact='121221')

    def test_room_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/room/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    # def test_room_add_api(self):
    #     self.client.login(email='kos@mail.ru', password='1234')
    #
    #     url = '/api/room/'
    #
    #     data = {
    #         'cinema': [self.cinema.id],
    #         'title': 'Big room',
    #
    #     }
    #     response = self.client.post(url, data=data, format='json')
    #     self.assertEqual(response.status_code, 201)

    def test_room_delete_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/room/'

        data = {
            'cinema': [self.cinema.id],
            'title': 'Big room',

        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_room_api_fail(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/room/'

        data = {
            'cinema': [self.cinema.id],
            'title': 1212,

        }
        with self.assertRaises(TypeError):
            Room.objects.create(data, url)


class TestMovieApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos@mail.ru', password='1234')

    def test_movie_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/movie/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_movie_add_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/movie/'

        data = {
            'title': 'Harry Potter',
            'description': 'film',

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_movie_delete_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/movie/'

        data = {
            'title': 'Harry Potter',
            'description': 'film',

        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_movie_api_fail(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/movie/'

        data = {
            'title': 'Harry Potter' * 200,
            'description': 'film',

        }
        with self.assertRaises(TypeError):
            Movie.objects.create(data, url)


class TestSeatApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos@mail.ru', password='1234')

    def test_seat_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/seat/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_seat_add_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/seat/'

        data = {
            'number_row': '12',
            'number_seat': '12',

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_seat_delete_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/seat/'

        data = {
            'number_row': '12',
            'number_seat': '12',

        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_seat_api_fail(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/seat/'

        data = {
            'title': 12 * 200,
            'description': 'film',

        }
        with self.assertRaises(TypeError):
            Seat.objects.create(data, url)


class TestShowTimeApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos@mail.ru', password='1234')
        cls.movie = Movie.objects.create(title='Harry Potter', description='film')

    def test_show_time_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/show_time/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_show_time_add_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/show_time/'

        data = {
            'movie': self.movie.id,
            'time': '12',

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_show_time_delete_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/show_time/'

        data = {
            'movie': self.movie.id,
            'time': '12',

        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_show_time_api_fail(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/show_time/'

        data = {
            'movie': self.movie.id,
            'time': '@*&$*#',

        }
        with self.assertRaises(TypeError):
            ShowTime.objects.create(data, url)


class TestTicketApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos', password='1234')
        cls.seat = Seat.objects.create(number_row='12', number_seat='12')
        cls.movie = Movie.objects.create(title='Harry Potter', description='film')

    def test_ticket_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/ticket/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_ticket_add_api(self):
        self.client.login(username='kos', password='1234')
        self.showtime = ShowTime.objects.create(time='12', movie=self.movie)

        url = '/api/ticket/'

        data = {
            'price': 12,
            'seat': self.seat.id,
            'show_time': self.showtime.id,

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_ticket_delete_api(self):
        self.client.login(username='kos@mail.ru', password='1234')
        self.showtime = ShowTime.objects.create(time='12', movie=self.movie)

        url = '/api/ticket/'

        data = {
            'price': 12,
            'seat': self.seat.id,
            'show_time': self.showtime.id,
        }

        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_ticket_api_fail(self):
        self.showtime = ShowTime.objects.create(time='12', movie=self.movie)

        url = '/api/ticket/'

        data = {
            'price': 12,
            'show_time': self.showtime.id,
        }
        with self.assertRaises(TypeError):
            Ticket.objects.create(data, url)


class TestFeedbakApi(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_superuser(username='kos@mail.ru', password='1234')

    def test_feedback_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/feedback/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_feedback_add_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/feedback/'

        data = {
            'user': self.user.id,
            'comment': 'hello',

        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_feedback_delete_api(self):
        self.client.login(username='kos@mail.ru', password='1234')

        url = '/api/feedback/'

        data = {
            'user': self.user.id,
            'comment': 'hello',

        }
        response = self.client.delete(url, data=data, format='json')
        self.assertEqual(response.status_code, 204)

    def test_feedback_api_fail(self):
        url = '/api/feedback/'

        data = {
            'user': self.user.id,
            'comment': 'hello',
        }
        with self.assertRaises(TypeError):
            Feedback.objects.create(data, url)
