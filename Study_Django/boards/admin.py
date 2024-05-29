from django.contrib import admin
from .models import Board
# Register your models here.


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "writer", "likes", "reviews", "created_at", "updated_at"]
    list_filter = ["likes", "created_at", "updated_at"]
    search_fields = ["title", "content", "writer"]

    readonly_fields = ["writer", "created_at"]

    actions = ('increment_likes',)
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('추가 옵션', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    )

    list_per_page = 2

    def increment_likes(self, request, queryset):
        for board in queryset:
            board.likes += 1
            board.save()
    increment_likes.short_description = '선택한 게시글 좋아요 수 증가'
