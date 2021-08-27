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

    def get_queryset(self):
        author_filter = self.request.GET.get('author')
        text_filter = self.request.GET.get('text')
        rating_filter = self.request.GET.get('rating')
        sort = self.request.GET.getlist('sort')        
        object_list = Feedback.objects.filter(
            Q(author__icontains=author_filter) & Q(text__icontains=text_filter) & Q(rating__icontains=rating_filter)
        ).order_by(*sort)
        return object_list
