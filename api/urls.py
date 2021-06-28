from api import views
from rest_framework import routers
from django.urls import path
from django.urls import include


router = routers.DefaultRouter()
router.register(r'feedbacks', views.FeedbackViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
