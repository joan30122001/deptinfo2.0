from django.shortcuts import render
from django.contrib.auth.models import User
from .models import TB_Information, TB_Event, TB_Partenaire
from enseignement.models import TB_Pole, TB_Ue, TB_Enseignant
from blog.models import TB_Article
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from django.utils.translation import gettext as _

from django.http import HttpResponseRedirect
from .forms import RegisterForm

from django.contrib import messages

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from enseignement.models import TB_Etudiant
from django.contrib import messages

# Create your views here.

def home(request):
    list_poles = TB_Pole.objects.all().order_by('-id')[:4]
    list_courses = TB_Ue.objects.all().order_by('-id')[:3]
    list_events = TB_Event.objects.all().order_by('date')[:3]
    list_teachers = TB_Enseignant.objects.all().order_by('id')[:6]
    list_articles = TB_Article.objects.all().order_by('-created_at')[:3]

    context = {
        "liste_poles": list_poles,
        "liste_cours": list_courses,
        "liste_evenements": list_events,
        "liste_enseignants": list_teachers,
        "liste_articles": list_articles
    }
    return render(request, 'barbillard/home.html', context)





def info(request):
    search_info = request.GET.get('searched')
    context = {}
    if search_info:
        list_infos = TB_Information.objects.filter(Q(title__icontains = search_info, published = True))
    else:
        list_infos = TB_Information.objects.filter(Q(published = True))

    page = request.GET.get('page', 1)
    paginator = Paginator(list_infos, 10)

    try:
        infos = paginator.page(page)
    except PageNotAnInteger:
        infos = paginator.page(1)
    except EmptyPage:
        infos = paginator.page(paginator.num_pages)

    context = {"liste_infos": infos, "searched": search_info}
    return render(request, "barbillard/infos.html", context)



def detail_info(request, slug_text):
    try:
        info = TB_Information.objects.get(Q(slug = slug_text, published = True))
    except TB_Information.DoesNotExist:
        raise Http404(_('Cet information n\' existe pas!!'))
    # category = info.category
    # info_en_relation = Information.objects.filter(category = category)
    return render(request, "barbillard/detail_info.html", {"info": info})



def barbillard_pdf(request):
    # Create Bystream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize = letter, bottomup = 0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add somelines of text
    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line 3"
    # ]

    # Designate The Model
    info = Information.objects.all()

    # Create Bank List
    lines = []

    for infos in info:
        lines.append(infos.title)
        lines.append(infos.body)
        lines.append(infos.Niveau)
        lines.append(infos.created_at)
        lines.append(infos.update_at)
        lines.append(infos.created_by)

    # Loops
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return Somethings
    return FileResponse(buf, as_attachment = True, filename = "barbillard.pdf")













def presentation(request):
    return render(request, 'barbillard/about.html')

def licence(request):
    return render(request, 'barbillard/licence.html')

def programme(request):
    return render(request, 'barbillard/programme.html')

def master(request):
    return render(request, 'barbillard/master.html')

def doctorat(request):
    return render(request, 'barbillard/doctorat.html')

def domaines(request):
    list_domains = TB_Pole.objects.all()
    context = {"liste_domaines": list_domains}
    return render(request, 'barbillard/domains.html', context)

def coordonnees(request):
    return render(request, 'barbillard/coordonnee.html')

def contact_page(request):
    return render(request, 'barbillard/contact.html')

def gdsc(request):
    return render(request, "barbillard/gdsc.html", {})

def comsas(request):
    return render(request, "barbillard/comsas.html", {})

def partenaire(request):
    partenaires = TB_Partenaire.objects.all()
    context = {'partenaires':partenaires}
    return render(request, "barbillard/partenaire.html", context)











# def courses(request):
#     search_course = request.GET.get('searched')
#     context = {}
#     if search_course:
#         list_courses = Ue.objects.filter(Q(title__icontains = search_course)).order_by('code')
#     else:
#         list_courses = Ue.objects.all().order_by('code')

#     page = request.GET.get('page', 1)
#     paginator = Paginator(list_courses, 10)

#     try:
#         courses = paginator.page(page)
#     except PageNotAnInteger:
#         courses = paginator.page(1)
#     except EmptyPage:
#         courses = paginator.page(paginator.num_pages)

#     context = {"liste_cours": courses, "searched": search_course}
#     return render(request, "barbillard/cours.html", context)


# def detail_course(request, slug_text):
#     try:
#         course = Ue.objects.get(slug = slug_text)
#     except Ue.DoesNotExist:
#         raise Http404('Ce cours n\' existe pas!!')
#     enseignants = Enseignant.objects.filter(ue = course)
#     niveau = course.Niveau
#     cours_en_relation = Ue.objects.filter(Niveau = niveau)[:4]
#     return render(request, "barbillard/detail_cours.html", {"cours": course, "enseignants": enseignants, "cer": cours_en_relation})














def event(request):
    
    search_evenement = request.GET.get('searched')
    context = {}
    if search_evenement:
        list_evenements = TB_Event.objects.filter(Q(title__icontains = search_evenement)).order_by('date')
    else:
        list_evenements = TB_Event.objects.all().order_by('date')

    page = request.GET.get('page', 1)
    paginator = Paginator(list_evenements, 10)

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context = {"liste_evenements": events, "searched": search_evenement}
    return render(request, "barbillard/evenement.html", context)



def detail_event(request, slug_text):
    try:
        event = TB_Event.objects.get(slug = slug_text)
    except Article.DoesNotExist:
        raise Http404('Cet ??v??nement n\' existe pas!!')
    event_en_relation = Event.objects.all().order_by('date')[:4]
    return render(request, "barbillard/detail_event.html", {"event": event, "eer": event_en_relation})



def event_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="event.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(title)
    p.drawString(description)
    p.drawString(speakers)
    p.drawString(created_at)


    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
















# def enseignant(request):
#     list_enseignants = Enseignant.objects.all()

#     p = Paginator(list_enseignants, 6)
#     page_num = request.GET.get('page', 1)
#     try:
#         page = p.page(page_num)
#     except EmptyPage:
#         page = p.page(1)

#     context = {"liste_enseignants": list_enseignants}
#     return render(request, "barbillard/enseignant.html", context)


# def detail_enseignant(request, slug_text):
#     try:
#         # text = slug_text.replace("-", " ")
#         ens = Enseignant.objects.get(slug = slug_text)
#     except Enseignant.DoesNotExist:
#         raise Http404('Cet enseignant n\' existe pas!!')
#     return render(request, "barbillard/detail_enseignant.html", {"ens": ens})











# def registerPage(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(
#                 request, f'Hi {username}, your account was created successfully')
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'barbillard/signup.html', {'form': form})






def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'barbillard/signup.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })

            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    # messages.error(request, 'Error. Email already exists..')
                    'error_message': 'Email already exists.'
                })

            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })

            # elif TB_Etudiant.objects.filter(email=form.clean_data['email'], matricule=form.clean_data['matricule'], is_active=False) is not None:
            #     return render(request, template, {
            #         'form': form,
            #         'error_message': 'You are not a student, if you are sure you are one please contact the admin at abdelmfossa@gmail.com .'
            #     })
                
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    # form.cleaned_data['matricule'],
                    # form.cleaned_data['niveau'],
                    # form.cleaned_data['phone'],
                    form.cleaned_data['password']
                )
                user.matricule = form.cleaned_data['matricule']
                user.niveau = form.cleaned_data['niveau']
                user.phone = form.cleaned_data['phone']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('barbillard/home')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})




def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                userSch = User.objects.get(email=email)
            except:
                userSch = None

            if userSch == None:
                messages.error(request, _('Utilisateur non trouv?? !'))
                return render(request, 'barbillard/login.html')
            else:
                username = userSch.username
                user = authenticate(
                    request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, _('Incorrect Email OR password'))

        context = {}
        return render(request, 'barbillard/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, _(
                'Your password was successfully updated!'))
            return redirect('change_password')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'information/change_password.html', {
        'form': form
    })