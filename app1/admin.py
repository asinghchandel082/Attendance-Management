from django.contrib import admin
from app1.models import Students, StudentDB, Attendance

# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Students, StudentsAdmin)


class StudentDBAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudentDB, StudentDBAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attendance, AttendanceAdmin)
