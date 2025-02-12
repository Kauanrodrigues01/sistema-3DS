from django.urls import path
from .views import home, get_teacher_data, success_page, get_teachers_data

app_name = 'teachers'

urlpatterns = [
    path('', home, name='home'),
    path('api/teacher/<int:teacher_id>/', get_teacher_data, name='get_teacher_data'),
    path('api/teachers/', get_teachers_data, name='get_teachers_data'),
    path('success/page/', success_page, name='success_page'),
    # path('<int:teacher_id>/', teacher_detail, name='teacher_detail'),
]