from django.contrib import admin
from .models import TB_Article, TB_Comment

# Register your models here.

admin.site.site_header = "Site Web du Département informatique UY1"

@admin.register(TB_Article)
class TB_ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image', 'user',)
    ordering = ('created_at',)
    list_filter = ('created_at', 'user',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()



@admin.register(TB_Comment)
class TB_CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'date_added', 'name', 'email', 'active',)
    ordering = ('-date_added',)
    list_filter = ('article', 'active',)
    search_fields = ('contain',)