from django.urls import include, path
from rest_framework import routers
from api import views
from django.urls import path

from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'room', views.RoomViewSet)
router.register(r'user', views.UserAPIView)
router.register(r'cinema', views.CinemaViewSet)
router.register(r'movie', views.MovieViewSet)
router.register(r'seat', views.SeatViewSet)
router.register(r'show_time', views.ShowTimeViewSet)
router.register(r'feedback', views.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('ticket/', views.TicketViewSet.as_view(), name='ticket'),

]
