from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


# view set の場合は simple/Default Routerを使う

app_name = 'api'

urlpatterns = [
    # ex: /api/courses/
    path('courses/', CoursesViewIndex.as_view(), name='courses_index'),

    # ex: /api/courses/1/
    path('courses/<int:pk>/', CoursesViewDetail.as_view(), name='courses_detail'),

    # ex: /api/issues/
    path('issues/', IssuesViewIndex.as_view(), name='issues_index'),

    # ex: /api/issues/1/
    path('issues/<int:pk>', IssuesViewDetail.as_view(), name='issues_detail'),
]
