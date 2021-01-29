from django.shortcuts import render, redirect
from django.conf import  settings
import os
import pandas as pd
from .func.drawpic import draw_pic
# Create your views here.
def homepage(request):
    context = {

    }
    return render(request,'home.html',context)

def filetransfer(request):
    return render(request, "filetransfer.html", locals())

def file_print(request):
    context = {

    }
    if request.method == "POST":
        if "check" in request.POST:
            #获取上传的文件
            file_obj = request.FILES.get("up_file")
            #获取当前项目的路径
            base = str(settings.BASE_DIR)
            # 文件本地存储地址
            path = os.path.join(base ,'myapp/static/file_upload',file_obj.name)
            # 将文件写入本地静态文件夹
            with open(path,'wb') as f1:
                for i in file_obj.chunks():
                    f1.write(i)
            # 读取上传的文件(内存中)
            df = pd.read_excel(file_obj)
            # 获取列名和值
            df1_head = df.columns.values.tolist()
            df1_values = df.values.tolist()
            # 返回列名和值的列表
            context = {
                'data_head': df1_head,
                'data_values': df1_values,
            }
            return render(request,'file_print.html',context)



def draw(request):
    imd = draw_pic()
    context = {
        'img': imd,
    }
    return render(request,'draw.html',context)