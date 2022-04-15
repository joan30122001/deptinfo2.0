from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from barbillard.views import (
    info,
    detail_info,
    barbillard_pdf,
    presentation,
    licence,
    domaines,
    contact_page,
    coordonnees,
    partenaire,
    master,
    doctorat,
    programme,
    gdsc,
    comsas,
    galerie,
    # courses,
    # detail_course,
    event,
    detail_event,
    event_pdf,
    # enseignant,
    # detail_enseignant,
    # registerPage,
    user_register,
    # teacher_register,
    user_login,
    logoutUser,
    change_password,
    )

app_name = 'barbillard'

urlpatterns = [
    path('barbillard/', info, name = "info"),
    path('barbillard/<slug:slug_text>/', detail_info, name = "detail_info"),
    path('barbillard_pdf', barbillard_pdf, name = "barbillard_pdf"),

    path('presentation-departement-informatique/', presentation, name = "presentation"),
    path('programme/licence-informatique/', licence, name = "licence"),
    path('nos-domaines/', domaines, name = "domaines"),
    path('contact/', contact_page, name = "contact"),
    path('coordonnees/', coordonnees, name = "coordonnees"),
    path('partenaire/', partenaire, name = "partenaire"),
    path('galerie/', galerie, name = "galerie"),
    path('programme/master-informatique/', master, name = "master"),
    path('programme/doctorat-informatique/', doctorat, name = "doctorat"),
    path('nos-programmes/', programme, name = "programme"),
    path('google-developer-student-club-uy1/', gdsc, name="gdsc"),
    path('computer-science-association/', comsas, name="comsas"),


    # path('cours/', courses, name = "courses"),
    # path('cours/<slug:slug_text>/', detail_course, name = "detail_course"),

    path('nos-evenements/', event, name = "event"),
    path('evenement/<slug:slug_text>/', detail_event, name = "detail_event"),
    path('event_pdf', event_pdf, name = "event_pdf"),

    # path('nos-enseignants/', enseignant, name = "enseignant"),
    # path('enseignant/<slug:slug_text>/', detail_enseignant, name = "detail_enseignant"),

    path('connexion/', views.user_login, name = "user_login"),
    # path('creer-compte/', registerPage, name = "registerPage"),
    path('creer-compte/', user_register, name = "user_register"),
    # path('teacher_creer-compte/', teacher_register, name = "teacher_register"),
    path('logout/', logoutUser, name = "logout"),
    path('change_password/', change_password, name = "change_password"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)