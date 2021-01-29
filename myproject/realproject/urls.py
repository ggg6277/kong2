from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('showindex/', views.showindex, name='showindex'),
    path('showdetail/<int:pk>', views.showdetail, name='showdetail'),
    path('image/', views.image, name='image'),
    path('main/', views.mainsite, name='mainsite'),
    path('apple/', views.apple, name='apple'),
    path('banana', views.banana, name='banana'),
    path('structure/', views.structure, name='structure'),
    path('product/', views.addproduct, name='addproduct'),
    path('productdetail/', views.product_detail, name='productdetail'),
    path('blog/', views.blog, name='blog'),
    path('base/', views.base, name='base'),
    path('blogs/', views.blog_index, name='blog_index'),
    path('blogs/<int:pk>', views.blog_detail, name='blog_detail'),
    path('blog_write/', views.blog_write, name='blog_write'),
    path('blogs/<category>/', views.blog_category, name='blog_category'),
    path('album/', views.album, name='album'),
    path('album_detail/<int:pk>', views.album_detail, name='album_detail')

]
