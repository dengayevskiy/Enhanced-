# -*- coding: utf-8 -*-
from __future__ import division
import math
import json

from django.http import HttpResponse
from django.shortcuts import render

from ..models.students import Student


# Views for students
def students_list(request):
    students = Student.objects.all()
    students_number = Student.objects.all().count()
    page_number = int(math.ceil(students_number / 3))
    if students_number > 3:
        students = Student.objects.all()[0:3]
    # try to order students list
    # order_by = request.GET.get('order_by', '')
    # if order_by in ('id', 'first_name', 'last_name', 'ticket'):page
    #     students = students.order_by(order_by)
    #     if request.GET.get('reverse', '') == '1':
    #         students = students.reverse()

    # paginate student
    # paginator = Paginator(students, 3)
    # page = request.GET.get('page')
    # try:
    #     students = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     students = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     students = paginator.page(paginator.num_pages)
    #
    return render(request, 'students/students_list.html',
                  {'students': students})


def ajax_test(request):
    results = {'success': False}

    # Тут — потрібні нам алгоритми
    if True:
        results = {'success': True, 'param1': 'Loaded', 'param2': 'moreeee'}

    json_data = json.dumps(results)
    return HttpResponse(json_data)


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student</h1>' % sid)
