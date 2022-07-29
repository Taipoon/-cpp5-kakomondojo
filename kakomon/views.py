from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Course


def index(request):
    """
    講義一覧を表示
    """
    courses = Course.objects.order_by('id')
    template = loader.get_template('courses/index.html')
    context = {
        'courses': courses,
    }
    return render(request, 'courses/index.html', context)
    # この記述は以下の記述と同じ
    # return HttpResponse(template.render(context, request))


def detail(request, course_id):

    # try:
    #    course = Course.objects.get(pk=course_id)
    # except Course.DoesNotExist:
    #    raise Http404('講義が存在しません')

    # get_list_or_404() は objects.filter() と同じ
    course = get_object_or_404(Course, pk=course_id)

    return render(request, 'courses/detail.html', {'course': course})
    # return HttpResponse(f'{course_id} の講義情報')


def create(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    try:
        created_issue = course.issue_set.create(
            title=request.POST['title'],
            content=request.POST['content'],
            lecture_number=request.POST['lecture_number'],
        )
        print(created_issue)
    except KeyError:
        return render(request, 'courses/detail.html',
                      {'course': course,
                       'error_message': '誤ったデータです'})
    else:
        return HttpResponseRedirect(reverse('courses:detail', args=(course.id, )))
