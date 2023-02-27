from django.contrib import admin

# Register your models here.
from apps.blog.models import Category, Post, Tag
from django import forms
from ckeditor.widgets import CKEditorWidget

class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Tag)
class TafAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ["title","created", "category", "is_draft"]
    list_filter = ["category", "is_draft", "created", ]
    filter_horizontal = ["tags"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ["name", "slug","id"]

