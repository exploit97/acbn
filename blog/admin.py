from django.contrib import admin
from .models import Post, Comment, Categorie,Partner,Documents

admin.site.register(Categorie)
admin.site.register(Post)
admin.site.register(Comment)

admin.site.register(Partner)
admin.site.register(Documents)