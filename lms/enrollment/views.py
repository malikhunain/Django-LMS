from django.shortcuts import render
from .models import Enrollment

# Create your views here.

def index(request):
    """
    Renders the enrollment index page with a list of all enrollments.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered HTML template with the enrollment list.
    """
    enrollment_list = Enrollment.objects.all()
    context = { 'enrollment_list': enrollment_list}
    return render(request, 'enrollment/index.html', context)


