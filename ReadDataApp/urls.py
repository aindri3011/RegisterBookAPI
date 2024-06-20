from django.urls import path
from ReadDataApp import views

urlpatterns = [
    path('getdetails/', views.get_student_summary_api.as_view()),
    path('getStudentdetails/', views.get_summary_from_phone.as_view()),
    path('getStudentList/', views.get_list_from_registrationDate.as_view()),
    path('getdetailsUsingEmail/',views.get_summary_from_email.as_view()),
]
