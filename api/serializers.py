from kakomon.models import Course, Issue, SampleAnswer
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'title', 'content', 'lecture_number', )


class SampleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        # Serializersに紐づけるmodelを定義する
        model = SampleAnswer

        fields = '__all__'

        extra_kwargs = {}

    def create(self, validated_data):
        sample_answer = SampleAnswer.objects.create(
            text=validated_data['text'],
            image=validated_data['image'],
            isssue_id=validated_data['issue_id'],
        )
        return sample_answer
