from django.forms import ModelForm
from polls.models import Feedback


class FeedbackForm(ModelForm):

    class Meta:
        model = Feedback
        fields = ('author', 'text', 'rating')
