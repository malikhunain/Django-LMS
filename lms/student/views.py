from django.shortcuts import render
from .models import Student

def student_list(request):
    """
    View function that retrieves all the students from the database and renders them in a template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object that contains the rendered template with the list of students.
    """
    student_list = Student.objects.all()
    context = { 'students': student_list}
    return render(request, 'student/student_list.html', context)

def student_profile(request, id):
    """
    This function takes a request object and a student id as input, 
    retrieves the corresponding student object from the database, 
    and renders the student profile page with the student object as context.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the student to retrieve.

    Returns:
        HttpResponse: The HTTP response object that contains the rendered student profile page.
    """
    student = Student.objects.get(pk=id)
    context = { 'student': student }
    return render(request, 'student/student_profile.html', context)