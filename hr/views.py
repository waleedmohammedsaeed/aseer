from django.shortcuts import render, redirect
from venv import logger
from django.views.generic.list import ListView
from django.forms import ValidationError
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.core.management import call_command
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
import os
# Create your views here.


class Hr_main_view(ListView):
    model = Employee
    template_name = 'hr/hr_main.html'
    context_object_name = 'employees'
    paginate_by = 10

   


# def empl(request):
#     employees = Employee.objects.filter()[:5]
#     return render(request, 'hr/employees.html', {'employees': employees})



# def hr(request):
#     return render(request, 'hr/employees.html')

def newemployee(request):
    eform = EmployeeForm()
    return render(request, 'hr/new_employee.html', {'eform': eform})

def emp(request):
    # emp = Employee.objects.all()
    eform = EmployeeForm()
    return render(request, 'emp.html', {'eform':eform})

def save_emp(request):
    if request.method == "POST":
        eform = EmployeeForm(request.POST)
        # print(request.POST)
        try:
            if eform.is_valid():
                eform.save()
                return redirect('/')
            else:
                print(eform.errors)
        except ValidationError as ve:
            # Handle specific ValueError
            logger.error(f"ValueError occurred: {str(ve)}")
            return JsonResponse({'error': f"ValueError: {str(ve)}"}, status=400)

        except KeyError as ke:
            # Handle missing keys in POST data
            logger.error(f"KeyError occurred: {str(ke)}")
            return JsonResponse({'error': f"KeyError: {str(ke)}"}, status=400)

        except Exception as e:
            # Catch any other exceptions
            logger.error(f"An unexpected error occurred: {str(e)}")
            return JsonResponse({'error': f"An error occurred: {str(e)}"}, status=500)
    return redirect('/')
    # return render(request, 'emp.html', {'eform':eform})


def import_actions(request):
    if request.method == 'POST':
        try:
            call_command('actions')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')


def import_area_side(request):
    if request.method == 'POST':
        try:
            call_command('areasides')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_eclass(request):
    if request.method == 'POST':
        try:
            call_command('eclass')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')


def import_general_specialization(request):
    if request.method == 'POST':
        try:
            call_command('general_sp')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_jobs(request):
    if request.method == 'POST':
        try:
            call_command('job')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_nationalities(request):
    if request.method == 'POST':
        try:
            call_command('nationality')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')

def import_specialization(request):
    if request.method == 'POST':
        try:
            call_command('rank')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')


def import_employees(request):
    if request.method == 'POST':
        try:
            call_command('emp')
            messages.success(request, "successfully imported")
        except Exception as e:
            messages.error(request, f'ERROR importing {e}')
        return redirect('/')
    else:
        redirect('/')
    return render(request, 'homepage.html')
