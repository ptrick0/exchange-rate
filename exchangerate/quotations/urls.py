from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="chart_plot"),
    path('quotation_by_dates/', views.quotation_by_dates, name="quotation_by_dates")
]
