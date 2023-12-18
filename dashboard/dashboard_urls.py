from django.urls import path
from .dashboard_views import dashboard_view
from .dashboard_views import assessment_selection_view, assessment_distribution_view, assessment_analysis_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('assessment_selection/', assessment_selection_view, name='assessment_selection'),
    path('assessment_distribution/', assessment_distribution_view, name='assessment_distribution'),
    path('assessment_analysis/', assessment_analysis_view, name='assessment_analysis'),
]
