from rest_framework import serializers
from polls.models import Feedback


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Feedback
        fields = ('id', 'author', 'text', 'rating')
