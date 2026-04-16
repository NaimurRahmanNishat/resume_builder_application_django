from django.contrib import admin
from myapp.models import Resume, Education, WorkExperience, Skill

# Register your models here.
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)
