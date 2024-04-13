from django.contrib import admin
from cinema.models import *
# Register your models here.

# 后台管理系统的使用：
#  1. 在这里注册对应的模型
#  2. 需要创建超级管理员的账号和密码： python manage.py createsuperuser
#  3. 根路由urls.py中添加： path('admin/', admin.site.urls),
#  4. 访问后台管理系统：http://127.0.0.1:8000/admin/
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(ScreeningRoom)
admin.site.register(Ticket)
