from django.contrib import admin
from blogging.models import Post, Category


class CategoryInLine(admin.TabularInline):
    """Defining an InlineModelAdmin object for the relationship"""
    # The 'through' attribute is a reference to the model that manages
    # the many-to-many relation.
    model = Category.posts.through


@admin.register(Post)  # registers our PostAdmin using a decorator
class PostAdmin(admin.ModelAdmin):
    """A ModelAdmin for Post. Overwrites the default admin interface."""
    # date_hierarchy = 'published_date'
    # empty_value_display = '-empty-'
    inlines = [CategoryInLine, ]


class CategoryAdmin(admin.ModelAdmin):
    """A ModelAdmin for Category. Declares included fields from model"""
    fields = ('name', 'description', )
    inlines = [CategoryInLine, ]


class CategoryAdmin(admin.ModelAdmin):
    """A ModelAdmin for Category. Declares excluded fields from model"""
    exclude = ('posts', )


admin.site.register(Category, CategoryAdmin)  # registers our PostAdmin

