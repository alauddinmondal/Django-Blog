from django.contrib import admin
from posts.models import Posts, myCategory
from django.contrib.auth.models import User, Group


# Register your models here.
class myAdminsite(admin.AdminSite):
    site_header = 'Alauddin Django'
    site_title = 'Alauddin Django Site'
    index_title = 'Alauddin Mondal Dashboard'


class PostAdmin(admin.ModelAdmin):
    
    def change_status_p(self,request,queryset):
        queryset.update(status='p')
    change_status_p.short_description = 'Publish Selected Posts'

    def change_status_d(self,request,queryset):
        queryset.update(status='p')
    change_status_d.short_description = 'Publish Drafted Posts'

    def change_status_w(self,request,queryset):
        queryset.update(status='p')
    change_status_w.short_description = 'Withdraw Selected Posts'

    list_display = ('id','title','show_content','user','show_thumbnail','status')
    list_display_links = ()
    list_filter = ('title',)
    # list_select_related = False
    list_per_page = 10
    list_max_show_all = 20
    list_editable = ('title','status')
    search_fields = ('title',)
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    preserve_filters = True
    inlines = []

    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    popup_response_template = None

    # Actions
    actions = ['change_status_p','change_status_d','change_status_w']
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    date_hierarchy = None
    save_as = False
    save_as_continue = True
    save_on_top = False
    preserve_filters = True
    inlines = []

    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    popup_response_template = None

    # Actions
    actions = []
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True


# admin.site.register(Posts, PostAdmin)
# admin.site.register(myCategory, CategoryAdmin)

admin_site = myAdminsite()
admin_site.register([User,Group]) 
admin_site.register(Posts, PostAdmin)
admin_site.register(myCategory, CategoryAdmin)