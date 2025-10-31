from django.contrib import admin
from .models import ProfilUser, PostUserMedia, PostUserVente


@admin.register(ProfilUser)
class ProfilUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'created_at']
    search_fields = ['user__username', 'bio']
    list_filter = ['created_at']


@admin.register(PostUserMedia)
class PostUserMediaAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'created_at']
    search_fields = ['user__username', 'description']
    list_filter = ['created_at']


@admin.register(PostUserVente)
class PostUserVenteAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'prix', 'whatsapp', 'created_at']
    search_fields = ['user__username', 'description']
    list_filter = ['created_at', 'prix']
