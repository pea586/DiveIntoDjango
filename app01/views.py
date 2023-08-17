from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world')

def user_list(request):
    # 按照Django自建的project，因为settings里的dir设置，会优先到根目录的template寻找，找不到再到App里的template寻找
    return render(request,'user_list.html') # 默认去App目录下找user_list模板（根据App的注册顺序，逐一去他们的template里寻找）

def user_add(request):
    return render(request,'user_add.html')