from django.contrib import admin
from django.urls import path, include
from user_management.user_management_views import login_view

# Modify your urlpatterns list in urls.py to include the user_management URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('dashboard/', include('dashboard.dashboard_urls')),
    path('user_management/', include('user_management.user_management_urls')),  # Add this line
    # Keep other URLs as they are
]
