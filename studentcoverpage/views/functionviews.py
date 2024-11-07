from django.shortcuts import render
from studentcoverpage.models import Student

def coverpage(request):

    students = Student.objects.all()
    context = {
        'students': students,
        'message' : 'This is Functionview'
    }
    return render(request, 'coverpage/cover.html', context)
