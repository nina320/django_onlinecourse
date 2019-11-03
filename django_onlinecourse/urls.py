# 解析使用者在瀏灠器輸入的url, 根據解析過後的結果，去指派某一支特定的程
# 式來做運作


"""django_onlinecourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from ledger import views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),  # 輸入一個url網址後，它會判斷這個網
    # 址符不符合第一個參數(如 'HFCadmin/')這樣的pattern, 若有符合，就會指派後面
    # (如 admin.site.urls )的這個程式去做運作
    # path('hello/', views.hello),  # 前面是pattern, 後面是某個app底下的views
    # 上面有增加 from ledger import views，所以我們在網址列輸入 localhost:8000/Hello/時，會呼叫
    # ledger底下的views.hello這個function
    # path('', views.b_dashboard),
    path('', include('ledger.urls')),  #只要遇到空白的url, 就去找ledger底下的urls.py
    path('accounts/login/', auth_views.LoginView.as_view()),  # 使用Django內建的login/logout function, 
    # Django要求要在templates底下有一個registration資料夾，它的底下放login.html
    path('accounts/logout/', views.logout),
]


# admin.site.urls 這個程式的主要功能是它會返回後台管理界面去操作
# 執行python manage.py runserver 8000後，到 localhost:8000/admin/就會到後台管理登入頁面