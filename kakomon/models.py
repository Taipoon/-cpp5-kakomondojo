import re

from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10, null=True)
    academic_year = models.IntegerField('開講年度')
    semester = models.CharField('学期', max_length=4)
    credits = models.IntegerField('単位数')

    def __str__(self):
        return self.course_name

    def is_hands_on(self):
        return bool(re.fullmatch(r'.*実習.*', self.course_name))


class Issue(models.Model):
    title = models.TextField()
    content = models.TextField()
    lecture_number = models.IntegerField()
    course_id = models.ForeignKey(Course,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SampleAnswer(models.Model):
    issue_id = models.ForeignKey(Issue,
                                 on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.text
