# Generated by Django 3.2.7 on 2022-02-14 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbillard', '0002_auto_20220214_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_etudiant',
            name='Niveau',
        ),
        migrations.RemoveField(
            model_name='tb_etudiant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tb_ue',
            name='Niveau',
        ),
        migrations.DeleteModel(
            name='TB_Enseignant',
        ),
        migrations.DeleteModel(
            name='TB_Etudiant',
        ),
        migrations.DeleteModel(
            name='TB_Pole',
        ),
        migrations.DeleteModel(
            name='TB_Ue',
        ),
    ]