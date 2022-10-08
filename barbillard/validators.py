from django.utils.translation import gettext as _

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.xlsx', '.xls']
    if ext.lower() not in valid_extensions:
        raise ValidationError(_('Extention de fichier non supportée.'))