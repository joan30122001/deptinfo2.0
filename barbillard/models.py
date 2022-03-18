from django.db import models
from ckeditor.fields import RichTextField
from .validators import validate_file_extension
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from deptinfo.utils import unique_slug_generator
from django.utils.translation import gettext as _


class TB_Niveau(models.Model):
    
    NIVEAU_CHOICES = (
        ('INFOL1', _('LICENCE I')),
        ('INFOL2', _('LICENCE II')),
        ('INFOL3', _('LICENCE III')),
        ('INFOM1', _('MASTER I')),
        ('INFOM2', _('MASTER II')),
        ('ICT4DL1', _('LICENCE PRO I')),
        ('ICT4DL2', _('LICENCE PRO II')),
        ('ICT4DL3', _('LICENCE PRO III')),
        ('MASTERPRO', _('MASTER PRO')),
        ('DOCTORAT', _('DOCTORAT/PhD'))
    )

    level = models.CharField(max_length=10, choices=NIVEAU_CHOICES, default='INFOL1', unique=True)
    diffusion = models.EmailField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.level

    class Meta:
       verbose_name = _('TB_Niveau')
       verbose_name_plural = _('TB_Niveaux')


class TB_Information(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Titre"))
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), help_text=_("Ne pas modifier ce champ !!!"))
    body = RichTextField(verbose_name=_("Contenu"))
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    urgent = models.BooleanField(default=False, verbose_name=_("Urgent ?"))
    public = models.BooleanField(default=True, verbose_name=_("Information publique ?"))
    Niveau = models.ForeignKey(TB_Niveau, verbose_name=_("Niveau concerné"), on_delete=models.CASCADE, null=True, blank=True)
    piecejointe = models.FileField(upload_to='PDF/Infos/',
        verbose_name=_("Pièce Jointe (Document)"),
        null=True, blank=True,
        validators=[validate_file_extension],
        help_text=_("Importez un Document au format: <em>PDF, WORD ou EXCEL</em>.")
    )
    image = models.ImageField(upload_to='Images/Infos/', height_field=None, width_field=None, max_length=255, null=True, blank=True, verbose_name=_("Image"))
    video = models.FileField(upload_to='Vidéos/Infos/', verbose_name=_("Video"), null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    published = models.BooleanField(default=False, verbose_name=_("Publié ?"))

    class Meta: 
        ordering = ('-created_at',)
        verbose_name = _('TB_Information')
        verbose_name_plural = _('TB_Informations')

    def __str__(self):
        return self.title



# class TB_Ue(models.Model):
#     DOMAINE_CHOICES = (
#         ('FONDA', 'Fondamentale'),
#         ('SECU', 'Sécurité'),
#         ('RESEAUX', 'Réseaux'),
#         ('SI/GL', 'SI/GL'),
#         ('DS', 'Sciences de Données'),
#     )
#     SEMESTER_CHOICES = (
#         ('SEM1', 'Semestre 1'),
#         ('SEM2', 'Semestre 2'),
#     )
#     code = models.CharField(max_length=255)
#     title = models.CharField(max_length = 255)
#     slug = models.SlugField(max_length=255, verbose_name=_("Slug"), help_text=_("Ne pas modifier ce champ !!!"))
#     objectif = models.TextField(verbose_name="Objectif du Cours")
#     content = RichTextField(verbose_name="Contenu du Cours")
#     semester = models.CharField(max_length=35, choices=SEMESTER_CHOICES, default='SEM1')
#     hours = models.IntegerField(verbose_name="Nombre d'heures du Cours")
#     domaine = models.CharField(max_length=35, choices=DOMAINE_CHOICES, default='FONDA')
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     update_at = models.DateTimeField(auto_now=True, editable=False)
#     Niveau = models.ForeignKey(TB_Niveau, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='Images/UE/', height_field=None, width_field=None, max_length=255)
#     piecejointe = models.FileField(upload_to='PDF/UE/',
#         verbose_name="Syllabus",
#         null=True, blank=True,
#         validators=[validate_file_extension],
#         help_text="Importez un Document au format: <em>PDF, WORD ou EXCEL.</em>"
#     )

#     def __str__(self):
#         return self.code

#     class Meta: 
#         ordering = ('-created_at',)
#         verbose_name = _('UE')
#         verbose_name_plural = _('UEs')



# class TB_Pole(models.Model):
#     image = models.ImageField(upload_to='Images/Domaines/', height_field=None, width_field=None, max_length=255, default="Images/Domaines/a.jpg")
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, verbose_name=_("Slug"), help_text=_("Ne pas modifier ce champ !!!"))
#     description = RichTextField()

#     def __str__(self):
#         return self.title

#     class Meta: 
#         ordering = ('title',)
#         verbose_name = _('TB_Pole')
#         verbose_name_plural = _('TB_Poles')





# class TB_Etudiant(models.Model):
#     matricule = models.CharField(max_length=7, primary_key=True)
#     first_name = models.CharField(max_length = 255)
#     last_name = models.CharField(max_length = 255)
#     email = models.EmailField(max_length=250, unique=True)
#     telephone = models.CharField(max_length = 20, null=True, blank=True)
#     actif = models.BooleanField(default=False)
#     Niveau = models.ForeignKey(TB_Niveau, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     photo= models.ImageField(upload_to='Images/Etudiants/', default="Images/Etudiants/un.jpg", height_field=None, width_field=None, max_length=255, null=True, blank=True)

#     def __str__(self):
#         return self.matricule

#     class Meta: 
#         verbose_name = _('TB_Etudiant')
#         verbose_name_plural = _('TB_Etudiants')




# class TB_Enseignant(models.Model):

#     GRADE_CHOICES = (
#         ('VAC', 'Vacataire'),
#         ('ASSISTANT', 'Assistant'),
#         ('CC', 'Chargé(e) de Cours'),
#         ('MC', 'Maître de conférences'),
#         ('PR', 'Professeur')
#     )
#     SEXE_CHOICES = (
#         ('M', 'Masculin'),
#         ('F', 'Feminin')
#     )
#     TITRE_CHOICES = (
#         ('M.', 'Monsieur'),
#         ('Mme.', 'Madame'),
#         ('Ing.', 'Ingénieur'),
#         ('Dr.', 'Docteur'),
#         ('Pr.', 'Professeur')
#     )

#     titre = models.CharField(max_length=255, choices=TITRE_CHOICES, verbose_name="Titre", default='Dr.')
#     first_name = models.CharField(max_length=255, verbose_name=_("Prénom"))
#     last_name = models.CharField(max_length=255, verbose_name=_("Nom"))
#     photo = models.ImageField(upload_to='Images/Enseignants/', height_field=None, width_field=None, max_length=255, default="Images/Enseignants/a.jpg")
#     slug = models.SlugField(max_length=255, verbose_name=_("Slug"), help_text=_("Ne pas modifier ce champ !!!"))
#     sexe = models.CharField(max_length=10, choices=SEXE_CHOICES, default='M')
#     email = models.EmailField(max_length=250, unique=True, verbose_name=_("E-mail Institutionnelle"))
#     telephone = models.CharField(max_length=20, verbose_name=_("Numéro de Téléphone"), null=True, blank=True)
#     grade = models.CharField(max_length = 255, choices=GRADE_CHOICES, default='CC')
#     jury = models.ForeignKey(TB_Niveau, on_delete=models.CASCADE, null=True, blank=True)
#     facebook_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien Facebook"))
#     linkedin_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien LinkedIn"))
#     github_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien Github"))
#     twitter_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien Twitter"))
#     site_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien site perso"))
#     biographie = models.TextField(verbose_name=_("Bibliographie de l'enseignant"))
#     localisation = models.CharField(max_length = 255, verbose_name=_("Localisation du Bureau et Numéro de porte"))
#     ue = models.ManyToManyField(TB_Ue, db_table="Enseignement", verbose_name=_("UEs enseignées"), blank=True)
#     pole = models.ManyToManyField(TB_Pole, db_table="Enseignant_Poles", verbose_name=_("Ses Pôles"), blank=True)
#     actif = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.first_name

#     class Meta: 
#         verbose_name = _('TB_Enseignant')
#         verbose_name_plural = _('TB_Enseignants')




class TB_Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    description = RichTextField()
    speakers = models.ManyToManyField("barbillard.TB_Speaker", db_table="Presentation")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    lien = models.URLField(max_length=2000, null=True, blank=True)
    piecejointe = models.FileField(upload_to='PDF/Events/',
        verbose_name="Pièce Jointe (Document)",
        null=True, blank=True,
        validators=[validate_file_extension],
        help_text="Importez un Document au format: <em>PDF, WORD ou EXCEL</em>."
    )
    date = models.DateField(auto_now=False, verbose_name="Date de l'évènement", auto_now_add=False)
    begin = models.TimeField(auto_now=False, verbose_name="Heure de début", auto_now_add=False)
    lieu = models.CharField(max_length=255, verbose_name="Lieu")
    image = models.ImageField(upload_to='Images/Events/', height_field=None, width_field=None, max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        ordering = ('-date',)

    def __str__(self):
        return self.title



class TB_Speaker(models.Model):
    TITRE_CHOICES = (
        ('Mr.', 'Monsieur'),
        ('Mme.', 'Madame'),
        ('Ing.', 'Ingénieur'),
        ('Dr.', 'Docteur'),
        ('Pr.', 'Professeur')
    )

    titre = models.CharField(max_length=255, choices=TITRE_CHOICES, verbose_name="Titre", default='Dr.')
    first_name = models.CharField(max_length=255, verbose_name="Prénom")
    last_name = models.CharField(max_length=255, verbose_name="Nom")
    photo = models.ImageField(upload_to='Images/Speaker/', height_field=None, width_field=None, max_length=255, default="Images/Enseignants/a.jpg")
    email = models.EmailField(max_length=250, unique=True, verbose_name="Adresse E-mail")
    telephone = models.CharField(max_length=20, verbose_name="Numéro de Téléphone", null=True, blank=True)
    facebook_url = models.URLField(max_length=250, null=True, blank=True, verbose_name="Lien Facebook")
    linkedin_url = models.URLField(max_length=250, null=True, blank=True, verbose_name="Lien LinkedIn")
    github_url = models.URLField(max_length=250, null=True, blank=True, verbose_name="Lien Github")
    twitter_url = models.URLField(max_length=250, null=True, blank=True, verbose_name="Lien Twitter")
    site_url = models.URLField(max_length=250, null=True, blank=True, verbose_name="Lien site perso")
    biographie = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name




def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender = TB_Event)




class TB_Partenaire(models.Model):
    logo = models.ImageField(upload_to='Images/partenaires/', height_field=None, width_field=None, max_length=255)
    title = models.CharField(max_length=255)
    description = RichTextField()
    site_url = models.URLField(max_length=250, null=True, blank=True, verbose_name=_("Lien vers la plate forme"))
    active = models.BooleanField(default=True, verbose_name=_("Activer un partenaire"))

    def __str__(self):
        return self.title

    class Meta:
       verbose_name = _('TB_Partenaire')
       verbose_name_plural = _('TB_Partenaires')