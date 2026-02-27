from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from Dashboard.models import Student


# Create your views here.
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html',{'students':students})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course = request.POST.get('course')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        # DO NOT pass 'date' if your model doesn't have it
        Student.objects.create(
            image=image,
            name=name,
            course=course,
            age=age,
            gender=gender,
            email=email

        )
        return redirect('dashboard')

    return render(request, 'add_student.html')


def update_student(request, id, date_value=None):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.image = request.FILES.get('image')
        student.name = request.POST.get('name')
        student.course = request.POST.get('course')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.email = request.POST.get('email')
        student.save()

    return render(request, 'update_student.html',{"student":student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("dashboard")