from django.shortcuts import render
from .models import TB_Pole, TB_Ue, TB_Enseignant
from blog.models import TB_Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from django.utils.translation import gettext as _

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def courses(request):
    search_course = request.GET.get('searched')
    context = {}
    if search_course:
        list_courses = TB_Ue.objects.filter(Q(title__icontains = search_course)).order_by('code')
    else:
        list_courses = TB_Ue.objects.all().order_by('code')

    page = request.GET.get('page', 1)
    paginator = Paginator(list_courses, 10)

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    context = {"liste_cours": courses, "searched": search_course}
    return render(request, "enseigner/cours.html", context)


def detail_course(request, slug_text):
    try:
        course = TB_Ue.objects.get(slug = slug_text)
    except TB_Ue.DoesNotExist:
        raise Http404('Ce cours n\' existe pas!!')
    enseignants = TB_Enseignant.objects.filter(ue = course)
    niveau = course.Niveau
    cours_en_relation = TB_Ue.objects.filter(Niveau = niveau)[:4]
    return render(request, "enseigner/detail_cours.html", {"cours": course, "enseignants": enseignants, "cer": cours_en_relation})


def enseignant(request):
    list_enseignants = TB_Enseignant.objects.all()

    p = Paginator(list_enseignants, 6)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {"liste_enseignants": list_enseignants}
    return render(request, "enseigner/enseignant.html", context)


def detail_enseignant(request, slug_text):
    try:
        # text = slug_text.replace("-", " ")
        ens = TB_Enseignant.objects.get(slug = slug_text)
    except TB_Enseignant.DoesNotExist:
        raise Http404('Cet enseignant n\' existe pas!!')
    return render(request, "enseigner/detail_enseignant.html", {"ens": ens})