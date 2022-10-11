from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('api', views.PrimaryPropertyViewSet)

urlpatterns = [
    path('<slug:slug>/', views.index, name='primary-property'),
    path('api/', include(router.urls)),
]