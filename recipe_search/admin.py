from django.contrib import admin

from .models import Topics, Recipes

# Register your models here.


class TopicsAdmin(admin.ModelAdmin):
    pass


class RecipesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topics, TopicsAdmin)
admin.site.register(Recipes, RecipesAdmin)
