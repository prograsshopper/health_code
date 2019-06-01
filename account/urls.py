from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'users', views.UsersViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path('signup/', views.SignupView.as_view()),
]
