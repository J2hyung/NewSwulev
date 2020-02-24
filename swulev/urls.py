from django.contrib import admin
from django.urls import path, include
from swuapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('signup', signup, name='signup'),
    path('main/', main, name='main'),
    path('new/<lectureid>/', new, name='new'),
    path('create/<lectureid>/', create, name='create'),
    path('detail/<lectureid>/', detail, name='detail'),
    path('mypage/<int:board_id>/delete/', delete, name='delete'),
    path('mypage/', mypage, name='mypage'),
    path('main_search/',post_list,name='search'),
]
