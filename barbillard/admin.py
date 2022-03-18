from django.contrib import admin

from .models import TB_Niveau, TB_Information, TB_Event, TB_Speaker, TB_Partenaire

admin.site.register(TB_Niveau)
admin.site.register(TB_Information)
admin.site.register(TB_Event)
admin.site.register(TB_Speaker)
admin.site.register(TB_Partenaire)