from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'center', views.CenterViewSet)
router.register(r'category', views.CenterCategoryViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
]