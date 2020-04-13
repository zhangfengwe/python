from django.contrib import admin

# Register your models here.
from .models import Question

# 向管理员页面增加新建的app
admin.site.register(Question)
