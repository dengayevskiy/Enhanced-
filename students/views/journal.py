# -*- coding: utf-8 -*-
__author__ = 'dgaievskiy'

from django.shortcuts import render

# Views for journal
def students_journal(request):
    students_in_journal = (
        {'id': 1,
         'name': u'Джек Деніелс'},
        {'id': 2,
         'name': u'Джон Голт'},
        {'id': 3,
         'name': u'Джим Моррісон'}
    )
    return render(request, 'students/journal.html',
                  {'journal': students_in_journal})
