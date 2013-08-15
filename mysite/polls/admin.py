from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice	# Model being displayed.
	extra = 0	# Amount of extra choice fields added.

class PollAdmin(admin.ModelAdmin):
	# Adds titled fieldsets for elements. Also adds collapsable fields if specified.
	fieldsets = [
	    (None,
		{'fields': ['question']}),
	    ('Date Information',
		{'fields': ['pub_date'], 'classes': ['collapse']}),
	]

	inlines = [ChoiceInline]	# Adds inline choices to polls.

	# Poll Selection Page
	list_display = ('question', 'pub_date', 'was_published_recently')	# Displays specified fields and allows sorting.
	list_filter = ['pub_date']	# Adds a filter.
	search_fields = ['question']	# Adds a search field.

admin.site.register(Poll, PollAdmin)	# Makes poll option available in admin directory.
