from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'centers', views.CenterViewSet)
router.register(r'category', views.CenterCategoryViewSet)
router.register(r'programs', views.ProgramViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
]
