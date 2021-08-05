from django.contrib import admin
from .models import Post, Comment, Categorie,Partner,Documents


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'post_image', 'created_date', 'updated_date','snippet','categorie']



admin.site.register(Post, PostAdmin)

admin.site.register(Categorie)
admin.site.register(Comment)

admin.site.register(Partner)
admin.site.register(Documents)