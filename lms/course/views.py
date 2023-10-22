from django.shortcuts import render
from .models import Course
from student.models import Student

def course_list(request):
    """
    View function that retrieves all courses from the database and renders them in a template.

    Args:
        request: HttpRequest object representing the current request.

    Returns:
        HttpResponse object representing the HTTP response that will be sent to the client.
    """
    courses = Course.objects.all()
    context = { 'courses': courses}
    return render(request, 'course/course_list.html', context)

def course_details(request, id):
    """
    This function takes a request and an id as input parameters and 
    returns the course details and enrolled students for the given course id.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the course.

    Returns:
        HttpResponse: The HTTP response object containing the rendered 
        course details template with the course and enrolled students context.
    """
    course = Course.objects.get(pk=id)
    enrolled_students = Student.objects.filter(enrollment__course_id = id)
    context = { 
        'course': course,
        'enrolled_students': enrolled_students
    }
    return render(request, 'course/course_details.html', context)