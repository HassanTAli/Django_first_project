from django.contrib import admin
from .models import Movie, Cast, Categories, Review, ID


class MovieAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name','casts__first_name')
    list_display = ('name', 'watch_count', 'likes', 'rate','custom_list_field')
    readonly_fields = ('custom_list_field',)
    
    fieldsets = (
       ["Section A",{"fields": ['name','description']}],
       [None,{
        "fields": ["likes","watch_count","rate",'custom_list_field']   
       }
        ],
       ["Attachment Section",{'fields': ['banner','video']}],
       ["Section D", {'fields':["casts"]}]
    )
    
    
    def custom_list_field(self,obj):
        if obj.likes and obj.watch_count:
            return '{} %'.format(100 * (obj.likes / obj.watch_count))


admin.site.register(Movie, MovieAdmin)
admin.site.register(Cast)
admin.site.register(Categories)
admin.site.register(Review)
admin.site.register(ID)
