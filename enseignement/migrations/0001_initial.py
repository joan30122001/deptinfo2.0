# Generated by Django 3.2.7 on 2022-10-05 21:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enseignement.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barbillard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TB_Pole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='Images/Domaines/a.jpg', max_length=255, upload_to='Images/Domaines/')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='Ne pas modifier ce champ !!!', max_length=255, verbose_name='Slug')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'TB_Pole',
                'verbose_name_plural': 'TB_Poles',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='TB_Ue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='Ne pas modifier ce champ !!!', max_length=255, verbose_name='Slug')),
                ('objectif', models.TextField(verbose_name='Objectif du Cours')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenu du Cours')),
                ('semester', models.CharField(choices=[('SEM1', 'Semestre 1'), ('SEM2', 'Semestre 2')], default='SEM1', max_length=35)),
                ('hours', models.IntegerField(verbose_name="Nombre d'heures du Cours")),
                ('domaine', models.CharField(choices=[('FONDA', 'Fondamentale'), ('SECU', 'Sécurité'), ('RESEAUX', 'Réseaux'), ('SI/GL', 'SI/GL'), ('DS', 'Sciences de Données')], default='FONDA', max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(max_length=255, upload_to='Images/UE/')),
                ('piecejointe', models.FileField(blank=True, help_text='Importez un Document au format: <em>PDF, WORD ou EXCEL.</em>', null=True, upload_to='PDF/UE/', validators=[enseignement.validators.validate_file_extension], verbose_name='Syllabus')),
                ('Niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbillard.tb_niveau')),
            ],
            options={
                'verbose_name': 'TB_UE',
                'verbose_name_plural': 'TB_UEs',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='TB_Etudiant',
            fields=[
                ('matricule', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, default='Images/Etudiants/un.jpg', max_length=255, null=True, upload_to='Images/Etudiants/')),
                ('Niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbillard.tb_niveau')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TB_Etudiant',
                'verbose_name_plural': 'TB_Etudiants',
            },
        ),
        migrations.CreateModel(
            name='TB_Enseignant',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('titre', models.CharField(choices=[('M.', 'Monsieur'), ('Mme.', 'Madame'), ('Ing.', 'Ingénieur'), ('Dr.', 'Docteur'), ('Pr.', 'Professeur')], default='Dr.', max_length=255, verbose_name='Titre')),
                ('first_name', models.CharField(max_length=255, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=255, verbose_name='Nom')),
                ('photo', models.ImageField(default='Images/Enseignants/a.jpg', max_length=255, upload_to='Images/Enseignants/')),
                ('slug', models.SlugField(help_text='Ne pas modifier ce champ !!!', max_length=255, verbose_name='Slug')),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], default='M', max_length=10)),
                ('email', models.EmailField(max_length=250, unique=True, verbose_name='E-mail Institutionnelle')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Numéro de Téléphone')),
                ('grade', models.CharField(choices=[('VAC', 'Vacataire'), ('ASSISTANT', 'Assistant'), ('CC', 'Chargé(e) de Cours'), ('MC', 'Maître de conférences'), ('PR', 'Professeur')], default='CC', max_length=255)),
                ('facebook_url', models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien Facebook')),
                ('linkedin_url', models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien LinkedIn')),
                ('github_url', models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien Github')),
                ('twitter_url', models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien Twitter')),
                ('site_url', models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien site perso')),
                ('biographie', models.TextField(verbose_name="Bibliographie de l'enseignant")),
                ('localisation', models.CharField(max_length=255, verbose_name='Localisation du Bureau et Numéro de porte')),
                ('actif', models.BooleanField(default=False)),
                ('jury', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='barbillard.tb_niveau')),
                ('pole', models.ManyToManyField(blank=True, db_table='Enseignant_Poles', to='enseignement.TB_Pole', verbose_name='Ses Pôles')),
                ('ue', models.ManyToManyField(blank=True, db_table='Enseignement', to='enseignement.TB_Ue', verbose_name='UEs enseignées')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TB_Enseignant',
                'verbose_name_plural': 'TB_Enseignants',
            },
        ),
    ]
