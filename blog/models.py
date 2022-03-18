from django.db import models
from ckeditor.fields import RichTextField
from .validators import validate_file_extension
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.translation import gettext as _

# Create your models here.

class TB_Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True, help_text=_("Ne pas modifier ce champ !!!"))
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    image = models.ImageField(upload_to='Images/Blog/', height_field=None, width_field=None, max_length=255)
    # category = models.CharField(max_length=255)
    piecejointe = models.FileField(upload_to='PDF/Events/',
        verbose_name="Pièce Jointe (Document)",
        null=True, blank=True,
        validators=[validate_file_extension],
        help_text="Importez un Document au format: <em>PDF, WORD ou EXCEL</em>."
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)

    class Meta: 
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class TB_Comment(models.Model):
    article = models.ForeignKey(TB_Article, on_delete=models.CASCADE, related_name="comments")
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    contain = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "Comment {} by {}".format(self.contain, self.name)

    class Meta:
        ordering = ['-date_added']