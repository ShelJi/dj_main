from django.contrib import admin
from dj_auto.models import Student, Teacher, Uploads


class UploadAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'uploaded_at']    

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Uploads, UploadAdmin)