from django.urls import path

from .views.functionviews import coverpage

from .views.classview import studentlistview

urlpatterns = [
    
    #function
    path('function/',coverpage, name='coverpage'),          

    #Class
    path('class/', studentlistview.as_view(), name='student_class'),
]

