from polls.models import Feedback
from django.views.generic import ListView, CreateView
from django.db.models import Q


# отправка отзыва
class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = 'create.html'
    fields = ['author', 'text', 'rating']


# получение и сортировка отзывов
class FeedbacksListView(ListView):
    model = Feedback
    template_name = 'browse_and_filter.html'
    paginate_by = 10

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
