from django.db import models
from ckeditor.fields import RichTextField
from .validators import validate_file_extension
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from deptinfo.utils import unique_slug_generator
from django.utils.translation import gettext as _
from barbillard.models import TB_Niveau


class TB_Ue(models.Model):
    DOMAINE_CHOICES = (
        ('FONDA', 'Fondamentale'),
        ('SECU', 'Sécurité'),
        ('RESEAUX', 'Réseaux'),
        ('SI/GL', 'SI/GL'),
        ('DS', 'Sciences de Données'),
    )
    SEMESTER_CHOICES = (
        ('SEM1', 'Semestre 1'),
        ('SEM2', 'Semestre 2'),
    )
    code = models.CharField(max_length=255)
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), help_text=_("Ne pas modifier ce champ !!!"))
    objectif = models.TextField(verbose_name="Objectif du Cours")
    content = RichTextField(verbose_name="Contenu du Cours")
    semester = models.CharField(max_length=35, choices=SEMESTER_CHOICES, default='SEM1')
    hours = models.IntegerField(verbose_name="Nombre d'heures du Cours")
    domaine = models.CharField(max_length=35, choices=DOMAINE_CHOICES, default='FONDA')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    Niveau = models.ForeignKey(TB_Niveau, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/UE/', height_field=None, width_field=None, max_length=255)
    piecejointe = models.FileField(upload_to='PDF/UE/',
        verbose_name="Syllabus",
        null=True, blank=True,
        validators=[validate_file_extension],
        help_text="Importez un Document au format: <em>PDF, WORD ou EXCEL.</em>"
    )

    def __str__(self):
        return self.code

    class Meta: 
        ordering = ('-created_at',)
        verbose_name = _('TB_UE')
        verbose_name_plural = _('TB_UEs')



class TB_Pole(models.Model):
    image = models.ImageField(upload_to='Images/Domaines/', height_field=None, width_field=None, max_length=255, default="Images/Domaines/a.jpg")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), help_text=_("Ne pas modifier ce champ !!!"))
    description = RichTextField()

    def __str__(self):
        return self.title

    class Meta: 
        ordering = ('title',)
        verbose_name = _('TB_Pole')
        verbose_name_plural = _('TB_Poles')





class TB_Etudiant(models.Model):
    matricule = models.CharField(max_length=7, primary_key=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=250, unique=True)
    telephone = models.CharField(max_length = 20, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    Niveau = models.ForeignKey(TB_Niveau, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    photo= models.ImageField(upload_to='Images/Etudiants/', default="Images/Etudiants/un.jpg", height_field=None, width_field=None, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.matricule

    class Meta: 
        verbose_name = _('TB_Etudiant')
        verbose_name_plural = _('TB_Etudiants')




class TB_Enseignant(models.Model):

    GRADE_CHOICES = (
        ('VAC', 'Vacataire'),
        ('ASSISTANT', 'Assistant'),
        ('CC', 'Chargé(e) de Cours'),
        ('MC', 'Maître de conférences'),
        ('PR', 'Professeur')
    )
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Feminin')
    )
    TITRE_CHOICES = (
        ('M.', 'Monsieur'),
        ('Mme.', 'Madame'),
        ('Ing.', 'Ingénieur'),
        ('Dr.', 'Docteur'),
        ('Pr.', 'Professeur')
    )

    code = models.CharField(max_length=7, primary_key=True)
    titre = models.CharField(max_length=255, choices=TITRE_CHOICES, verbose_name="Titre", default='Dr.')
    first_name = models.CharField(max_length=255, verbose_name=_("Prénom"))
    last_name = models.CharField(max_length=255, verbose_name=_("Nom"))
    photo = models.ImageField(upload_to='Images/Enseignants/', height_field=None, width_field=None, max_length=255, default="Images/Enseignants/a.jpg")
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), help_text=_("Ne pas modifier ce champ !!!"))
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='M')
    email = models.EmailField(max_length=250, unique=True, verbose_name=_("E-mail Institutionnelle"))
    telephone = models.CharField(max_length=20, verbose_name=_("Numéro de Téléphone"), null=True, blank=True)
    grade = models.CharField(max_length = 255, choices=GRADE_CHOICES, default='CC')
    jury = models.ForeignKey(TB_Niveau, on_delete=models.CASCADE, null=True, blank=True)
    facebook_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien Facebook"))
    linkedin_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien LinkedIn"))
    github_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien Github"))
    twitter_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien Twitter"))
    site_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien site perso"))
    biographie = models.TextField(verbose_name=_("Bibliographie de l'enseignant"))
    localisation = models.CharField(max_length = 255, verbose_name=_("Localisation du Bureau et Numéro de porte"))
    ue = models.ManyToManyField(TB_Ue, db_table="Enseignement", verbose_name=_("UEs enseignées"), blank=True)
    pole = models.ManyToManyField(TB_Pole, db_table="Enseignant_Poles", verbose_name=_("Ses Pôles"), blank=True)
    actif = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta: 
        verbose_name = _('TB_Enseignant')
        verbose_name_plural = _('TB_Enseignants')