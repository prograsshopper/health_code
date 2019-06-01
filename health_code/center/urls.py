from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'center', views.CenterViewSet)
router.register(r'category', views.CenterCategoryViewSet)
router.register(r'category', views.ProgramViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
]