from django.urls import path
from . import views
from .views import Hr_main_view

from . import views
app_name = "hr"
urlpatterns = [
    # path('', views.empl, name='hr'),
    path('', Hr_main_view.as_view(), name='hr'),
    path('new', views.newemployee, name="newemployee"),


    path('emp', views.emp, name='emp'),
    path('save_emp', views.save_emp, name='save_emp'),

    path('import_actions', views.import_actions, name='import_actions'),
    path('import_area_side', views.import_area_side, name='import_area_side'),
    path('import_area_side', views.import_area_side, name='import_area_side'),
    path('import_eclass', views.import_eclass, name='import_eclass'),
    path('import_general_specialization', views.import_general_specialization, name='import_general_specialization'),
    path('import_jobs', views.import_jobs, name='import_jobs'),
    path('import_nationalities', views.import_nationalities, name='import_nationalities'),
    path('import_specialization', views.import_specialization, name='import_specialization'),

    path('import_employees', views.import_employees, name='import_employees'),
]