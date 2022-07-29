from django.test import TestCase

from .models import Course


class CourseModelTests(TestCase):
    def test_is_hands_on_true(self):
        """
        講義名に「実習」を含む場合Trueを返します
        """
        course = Course(course_name='サイバーセキュリティ実習A',
                        academic_year=3,
                        semester='1-2',
                        credits=2)
        course.save()
        self.assertTrue(course.is_hands_on())

    def test_is_hands_on_false(self):
        course = Course(course_name='ネットワーク演習',
                        academic_year=2,
                        semester='3',
                        credits=2)
        course.save()
        self.assertFalse(course.is_hands_on())
