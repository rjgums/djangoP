from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.indexgender),
    path('genders/create', views.creategender),
    path('store_gender', views.storegender),
    path('genders/show/<int:gender_id>', views.showgender),
    path('genders/edit/<int:gender_id>', views.editgender),
    path('genders/update/<int:gender_id>', views.updategender),
    path('genders/delete/<int:gender_id>', views.deletegender),
    path('genders/destroy/<int:gender_id>', views.destroygender),
    path('users', views.index_user),
    path('users/create', views.create_user),
    path('users/store', views.store_user),
    path('users/show/<int:user_id>', views.show_user),
    path('users/edit/<int:user_id>', views.edit_user),
    path('users/update/<int:user_id>', views.update_user),
    path('users/delete/<int:user_id>', views.delete_user),
    path('users/destroy/<int:user_id>', views.destroy_user),
    path('sections', views.index_section),
    path('sections/create', views.create_section),
    path('section/store', views.store_section),
    path('section/show/<int:section_id>', views.show_section),
    path('section/edit/<int:section_id>', views.edit_section),
    path('section/update/<int:section_id>', views.update_section),
    path('section/delete/<int:section_id>', views.delete_section),
    path('section/destroy/<int:section_id>', views.destroy_section),
    path('years', views.index_year),
    path('years/create', views.create_year),
    path('year/store', views.store_year),
    path('year/show/<int:year_id>', views.show_year),
    path('year/edit/<int:year_id>', views.edit_year),
    path('year/update/<int:year_id>', views.update_year),
    path('year/delete/<int:year_id>', views.delete_year),
    path('year/destroy/<int:year_id>', views.destroy_year),
    path('courses', views.index_course),
    path('courses/create', views.create_course),
    path('course/store', views.store_course),
    path('course/show/<int:course_id>', views.show_course),
    path('course/edit/<int:course_id>', views.edit_course),
    path('course/update/<int:course_id>', views.update_course),
    path('course/delete/<int:course_id>', views.delete_course),
    path('course/destroy/<int:course_id>', views.destroy_course),
    path('students', views.index_student),
    path('students/create', views.create_student),
    path('student/store', views.store_student),
    path('student/show/<int:student_id>', views.show_student),
    path('student/edit/<int:student_id>', views.edit_student),
    path('student/update/<int:student_id>', views.update_student),
    path('student/delete/<int:student_id>', views.delete_student),
    path('student/destroy/<int:student_id>', views.destroy_student),
    path('academics', views.index_academic),
    path('academics/create', views.create_academic),
    path('academic/store', views.store_academic),
    path('academic/show/<int:student_id>', views.show_academic),
    path('academic/edit/<int:student_id>', views.edit_academic),
    path('academic/update/<int:student_id>', views.update_academic),
    path('academic/delete/<int:student_id>', views.delete_academic),
    path('academic/destroy/<int:student_id>', views.destroy_academic),
]
