from django.views.generic import ListView
from studentcoverpage.models import Student

class studentlistview(ListView):

    model = Student
    template_name = 'coverpage/cover.html'
    context_object_name = 'students' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This is Class view'
        return context
