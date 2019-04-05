from django.contrib import admin

from .models import Article, Topic, Scope


class ScopeInline(admin.TabularInline):
    model = Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
