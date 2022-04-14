from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "quotations/chart_plot.html", context = {})