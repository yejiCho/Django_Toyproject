from django.contrib import admin
from .models import Fcuser
# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    # 괄호하고 , 해줘야함 그래야 tuple로 인식

admin.site.register(Fcuser,FcuserAdmin)
