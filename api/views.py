from rest_framework import generics

from .serializers import *
from kakomon.models import Course, Issue, SampleAnswer


# ListAPIView : GET 全件取得
class CoursesViewIndex(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# RetrieveAPIView : GET 一件取得
class CoursesViewDetail(generics.RetrieveAPIView):
    queryset = Course.objects.filter()
    serializer_class = CourseSerializer


class IssuesViewIndex(generics.ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssuesViewDetail(generics.RetrieveAPIView):
    queryset = Issue.objects.filter()
    serializer_class = IssueSerializer
