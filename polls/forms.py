from django.forms import ModelForm
from polls.models import Feedback
from django import forms


class FeedbackForm(ModelForm):
    author = forms.CharField(max_length=20, label="Автор")
    text = forms.CharField(max_length=120, label="Текст")
    rating = forms.IntegerField(min_value=1, max_value=5, label="Оценка")

    class Meta:
        model = Feedback
        fields = ('author', 'text', 'rating')
