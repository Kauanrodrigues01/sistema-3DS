from django.urls import path
from . import views

urlpatterns = [
    path('generate-report/csv/', views.download_csv_selections_report, name='download_csv_selections_report'),
    path('generate-report/excel/', views.download_excel_selections_report, name='download_excel_selections_report'),
]
