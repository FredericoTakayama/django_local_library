from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
# admin.site.register(Author)
#admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    model = Book
    fields = ('title', 'summary', 'genre')
    extra = 0 # don't show new lines to add new books instances

# define the admin class
# @admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
# Register the admin class with associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    fields = ['imprint', 'id', ('status', 'due_back')]
    extra = 0 # don't show new lines to add new books instances

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
# admin.site.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    # fields = ['book', 'imprint', 'id', ('status', 'due_back')]
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': [('status', 'due_back', 'borrower')]
        }),
    )
# admin.site.register(BookInstance, BookInstanceAdmin)

admin.site.register(Genre)
admin.site.register(Language)