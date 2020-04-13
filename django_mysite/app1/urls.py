# app1应用的请求路径

from . import views
from django.urls import path, re_path

# 用于模板中为url名称添加命名空间
app_name = 'app1'

urlpatterns = [
    path(r'index', views.IndexView.as_view(), name='index'),
    # detailView通用视图会获取url中的pk参数值，所以将question_id修改为pk
    re_path(r'detail/(?P<pk>[0-9])$', views.DetailView.as_view(), name='detail'),
    re_path(r'detail/(?P<question_id>[0-9])$', views.detail, name='detail'),
    path(r'add', views.add, name='add'),
    path(r'showadd', views.showadd, name='showadd')
]