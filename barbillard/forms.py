from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from enseignement.models import TB_Etudiant, TB_Enseignant

class CreateUserForm(UserCreationForm):
	class Meta:
		model = TB_Etudiant
		fields = ['first_name', 'matricule', 'Niveau', 'telephone', 'email', 'password1', 'password2']


# class CreateTeacherForm(UserCreationForm):
#     class Meta:
#         model = TB_Enseignant
#         # fields = ['first_name', 'code', 'email', 'password1', 'password2']
#         fields = ('__all__')


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
	    model = User
	    fields = ['email']


LEVEL_CHOICES =(
    ("Informartique 1", "Informartique 1"),
    ("Informartique 2", "Informartique 2"),
    ("Informartique 3", "Informartique 3"),
    ("Master 1", "Master 1"),
    ("Master 2", "Master 2"),
    ("ICT L1", "ICT L1"),
    ("ICT L2", "ICT L2"),
    ("ICT L3", "ICT L3"),
    ("Master Pro", "Master Pro"),
)   
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': "Votre nom d'utilisateur..."}))
    matricule = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': "Votre matricule..."}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': "Votre adresse email..."}))
    niveau = forms.ChoiceField(choices = LEVEL_CHOICES, widget=forms.Select(attrs={'class':'form-control', 'placeholder': "Votre niveau..."}))
    phone = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': "Votre numero de téléphone..."}), required = True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': "Votre mot de passe..."}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': "Votre mot de passe..."}))



# class TeacherForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))