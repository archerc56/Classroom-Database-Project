from django.contrib import admin

# Register your models here.
from .models import Assigned, Assignment, DisciplinaryReport, IstationProgram, Student, WeeklyLessonPlan 

admin.site.register(Assigned)
admin.site.register(Assignment)
admin.site.register(DisciplinaryReport)
admin.site.register(IstationProgram)
admin.site.register(Student)
admin.site.register(WeeklyLessonPlan)

