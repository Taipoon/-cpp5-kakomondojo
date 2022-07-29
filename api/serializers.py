from rest_framework import serializers

from kakomon.models import Course, Issue, SampleAnswer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        # fields = '__all__'
        fields = ('id', 'title', 'content', 'lecture_number', )


class SampleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleAnswer
        # Serializersに紐づけるmodelを定義する

        fields = '__all__'

        extra_kwargs = {

        }
