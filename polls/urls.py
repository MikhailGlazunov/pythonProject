from django.urls import path
from polls.views import FeedbacksListView, FeedbackCreateView
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='create/')),
    path('browse_and_filter/', FeedbacksListView.as_view(), name='browse_and_filter'),
    path('create/', FeedbackCreateView.as_view(), name='create'),
]
