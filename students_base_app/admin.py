from django.contrib import admin
from students_base_app.models import Student, Group, ModelsLogger


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birthdate', 'studentid_cart', 'group']
    search_fields = ['full_name', 'studentid_cart']
    list_per_page = 20
    list_filter = ['group']

    class Meta:
        model = Student


class StudentAdminInline(admin.TabularInline):
    model = Student
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'get_group_monitor']
    search_fields = ['group_name']
    list_per_page = 20
    inlines = [StudentAdminInline]

    class Meta:
        model = Group


class ModelsLoggerAdmin(admin.ModelAdmin):
    list_display = ['application', 'model', 'operation_type', 'timestamp']

    class Meta:
        model = ModelsLogger


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(ModelsLogger, ModelsLoggerAdmin)
