from django.contrib import admin

from .models import Post
class PostAdmin(admin.ModelAdmin):
	fields=['published','title','content','author','slug']
	list_display=('published','title','updated_at')
	list_display_links=['title']
	list_editable=['pulished']
	list_filter=['published'.'updated_at']
	prepopulated_field=('title',)
	search_fields=['title','content']

admin.site.register(Post,PostAdmin)
