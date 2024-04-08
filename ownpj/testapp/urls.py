from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('rating_page',views.firstpage, name="firstpage"),
    path('product',views.secpage,name="secpage"),
    path('lastitem', views.thirdpage,name='lastitem'),
    path('end', views.lastpage, name="end")
]