"""punterspal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from diary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_landing_page, name='landing-page'),
    # path('sign-up', views.get_sign_up_page, name='sign-up'),
    path('accounts/', include('allauth.urls')),
    path('create_new_entry', views.NoteDetail.as_view(), name='new-entry'),
    path('diary_display.html', views.ShowDiaryEntries.as_view(), name='all-entries'),
    path('edit_entry/<entry_id>', views.EditDiaryEntry.as_view(), name='edit-entry'),
    path('delete_entry/<entry_id>', views.delete_entry, name='delete-entry'),
    path('search_results.html', views.SearchResults.as_view(), name='search-results'),
]

handler404 = "diary.views.error_404_view"
