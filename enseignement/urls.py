from django.urls import path, include
from enseignement.views import courses, detail_course, enseignant, detail_enseignant

app_name = "enseignement"

urlpatterns = [
    path('cours/', courses, name = "courses"),
    path('cours/<slug:slug_text>/', detail_course, name = "detail_course"),
    path('nos-enseignants/', enseignant, name = "enseignant"),
    path('enseignant/<slug:slug_text>/', detail_enseignant, name = "detail_enseignant"),
]