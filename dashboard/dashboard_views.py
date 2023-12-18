from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def assessment_selection_view(request):
    # Placeholder view for Assessment Selection
    return HttpResponse('<h1>Assessment Selection</h1>')

@login_required
def assessment_distribution_view(request):
    # Placeholder view for Assessment Distribution
    return HttpResponse('<h1>Assessment Distribution</h1>')

@login_required
def assessment_analysis_view(request):
    # Placeholder view for Assessment Analysis
    return HttpResponse('<h1>Assessment Analysis</h1>')
