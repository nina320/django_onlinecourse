# 此為後台管理程式，可在此註冊我們在 models.py定義的table
# 之後打開後台管理界面時，就可對這些tables進行新增、修改、刪除…等動作


from django.contrib import admin
from .models import Category, Record

# Register your models here.
admin.site.register(Category)
admin.site.register(Record)
