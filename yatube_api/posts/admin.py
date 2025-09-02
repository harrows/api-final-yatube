from django.contrib import admin

from .models import Post, Comment, Group, Follow


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("id", "title", "slug")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "pub_date", "group")
    list_filter = ("pub_date", "group")
    search_fields = ("text",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "created")
    list_filter = ("created",)
    search_fields = ("text",)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "following")
    search_fields = ("user__username", "following__username")
