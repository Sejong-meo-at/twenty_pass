from django.conf.urls import url
from django.contrib import admin
from twentyPass import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^twentyPass/(?P<primaryKey>[0-9]+)/detail/$', views.detail, name="detail"),
    url(r'^twentyPass/addQuestion/$', views.add, name="add"),
]
