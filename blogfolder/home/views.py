from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Student
from .models import Student, Program

class HompageView(View):
    def get(self, request):
        return render(request, 'index.html')



def add_user(request):

    if request.method == 'POST':
        profile_image = request.POST['profile_image'] 
        full_name = request.POST['full_name']
        cohort = request.POST['cohort']
        date_joined = request.POST['date_joined']
        program_id = request.POST['program']
        rating = request.POST['rating']
        status = request.POST['status']

        # Create and save the Student instance
        new_student = Student(
            profile_image=profile_image,
            full_name=full_name,
            cohort=cohort,
            date_joined=date_joined,
            program=program_id,
            rating=rating,
            status_display=status
        )
        new_student.save() 
    
        # Save to the databas
        return redirect('home')  # Redirect after successful addition

from django.views.generic import View
from .models import Student

class HompageView(View):
    def get(self, request):
        users = Student.objects.all()  # Fetch all users
        return render(request, 'index.html', {'users': users})