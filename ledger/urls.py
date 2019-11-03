from django.urls import path
from . import views   # .代表當下這個路徑

urlpatterns = [     
    path('', views.b_dashboard),
    path('settings', views.settings),
    path('add_category', views.addCategory),
    path('delete_category/<str:category>', views.deleteCategory),
    path('add_record', views.addRecord),
    path('delete_record', views.deleteRecord),

]


# admin.site.urls 這個程式的主要功能是它會返回後台管理界面去操作
# 執行python manage.py runserver 8000後，到 localhost:8000/admin/就會到後台管理登入頁面