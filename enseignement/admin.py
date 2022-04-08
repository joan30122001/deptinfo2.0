from django.contrib import admin
from .models import TB_Niveau, TB_Ue, TB_Pole, TB_Etudiant, TB_Enseignant

# Register your models here.

admin.site.site_header = "Site Web du Département informatique UY1"
admin.site.register(TB_Pole)

# @admin.register(Niveau)
# class NiveauAdmin(admin.ModelAdmin):
#     list_display = ('level', 'diffusion',)
#     ordering = ('level',)
#     search_fields = ('level',)


@admin.register(TB_Etudiant)
class TB_EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'first_name', 'last_name', 'email', 'Niveau', 'is_active', 'user',)
    ordering = ('matricule',)
    list_filter = ('Niveau',)
    search_fields = ('matricule', 'first_name', 'last_name', 'email',)


@admin.register(TB_Ue)
class TB_UeAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'semester', 'domaine', 'Niveau',)
    ordering = ('-code',)
    list_filter = ('semester', 'domaine', 'Niveau',)
    search_fields = ('code', 'title',)


@admin.register(TB_Enseignant)
class TB_EnseignantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'grade', 'jury', 'actif', 'user',)
    ordering = ('first_name',)
    list_filter = ('pole', 'jury', 'actif',)
    search_fields = ('first_name', 'last_name', 'email',)
