from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback
from django.views.generic import ListView
from django.db.models import Q
from .serializers import FeedbackSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


def create(request):
    if request.method == "POST":
        feedbackform = FeedbackForm(request.POST)
        feedbackform.author = request.POST.get('author')
        feedbackform.text = request.POST.get('text')
        feedbackform.rating = request.POST.get('rating')
        if feedbackform.is_valid():
            feedbackform.save()
            return render(request, "create.html", {"form": feedbackform})
    else:
        feedbackform = FeedbackForm()
        return render(request, "create.html", {"form": feedbackform})


# получение и сортировка отзывов
class Filtering(ListView):
    model = Feedback
    template_name = 'browse_and_filter.html'

    def get_queryset(self):
        query1 = self.request.GET.get('q')
        query2 = self.request.GET.get('w')
        query3 = self.request.GET.get('e')
        object_list = Feedback.objects.filter(
            Q(author__icontains=query1) & Q(text__icontains=query2) & Q(rating__icontains=query3)
        )
        return object_list


# api
class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
