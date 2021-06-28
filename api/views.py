from api.serializers import FeedbackSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from polls.models import Feedback


# api
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.none()
    model = Feedback
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
