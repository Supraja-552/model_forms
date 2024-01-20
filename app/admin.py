from django.contrib import admin

# Register your models here.
from app.models import *
class Customize_webpage(admin.ModelAdmin):
    list_display=['topic_name','email','url','name']
    list_display_links=['name','email']
    list_editable=['url']
    list_display_per_page=2
   
class Customize_access(admin.ModelAdmin):
    list_display=['name','date','author']
    list_display_links=['name','date']
    list_editable=['author']
    list_per_page=2 
    
admin.site.register(Topic)
admin.site.register(Webpage,Customize_webpage)
admin.site.register(AccessRecord,Customize_access)
admin.site.site_header='Django'

admin.site.site_title='Django_title'
admin.site.index_title='Django'