from django.contrib import admin

from .models import Course, Issue, SampleAnswer


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('講義情報', {'fields': ['course_name', 'course_code']}),
        ('開講時期',
         {'fields': ['academic_year',
                     'semester']}),
        ('単位数', {'fields': ['credits']})
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Issue)
admin.site.register(SampleAnswer)
