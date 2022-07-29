from django.urls import path

from . import views


app_name = 'courses'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),

    # ex: /courses/1/
    path('courses/<int:course_id>/', views.detail, name='detail'),

    # ex: /courses/1/
    path('courses/<int:course_id>/create', views.create, name='create'),
]
