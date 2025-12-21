from django.shortcuts import render
from django.shortcuts import redirect
from .models import Student
# Create your views here.
def Student_list(request):
    student = Student.objects.all()
    return render(request, 'list.html', {'student':student})

def add_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']
        student = Student(
            name=name, 
            email=email, 
            age=age, 
            address=address
            )
        student.save()
        return redirect('Student_list')
    return render(request, 'form.html')

def edit_data(request ,id):
    student= Student.objects.get(id=id)
    if request.method == 'POST':
     student = request.POST
     name = student['name']
     age = student['age']
     email = student['email']
     address = student['address']
     student= Student.objects.get(id=id)
     student.name =name
     student.age=age
     student.email=email
     student.address=address
     student.save()
     return redirect('Student_list')
    return render(request, 'edit.html' , {'student': student})
def delete_data(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('Student_list')  # after deletion, go back to list

    # If GET request, show the delete confirmation page
    return render(request, 'delete.html', {'student': student})
