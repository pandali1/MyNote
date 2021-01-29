from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('filetransfer',views.filetransfer,name = 'filetransfer'),
    path('fileprint',views.file_print,name = 'fileprint'),
    path('draw',views.draw,name = 'draw')
]