from django.urls import path
from django.urls import include
from polls import views
from .views import Filtering
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'feedbacks', views.FeedbackViewSet)


urlpatterns = [
    path('1/', Filtering.as_view(), name='browse_and_filter'),
    path('', views.create),
    path('2/', include(router.urls)),
]
