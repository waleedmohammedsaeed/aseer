from django.contrib import admin
# from .models import Employee
from .models import Eclass, Nationality, Job, Specialization, GeneralSpecialization, Employee, Area_side, Actions, Employee

# Register your models here.

# admin.site.register(Employee)
admin.site.register(Eclass)
admin.site.register(Nationality)
admin.site.register(Job)
admin.site.register(Specialization)
admin.site.register(GeneralSpecialization)
admin.site.register(Area_side)
admin.site.register(Actions)

class AdminEmployee(admin.ModelAdmin):
    list_display = ('empno', 'ename', 'nationality', 'job_title', 'rank')


admin.site.register(Employee, AdminEmployee)
