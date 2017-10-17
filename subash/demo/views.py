# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UserForm


#def index(request):
#    return HttpResponse('You\'re at the index. <a href="/page">LMS page</a></br> <a href="/qispage">QIS page</a></br> <a href="/openid/logout">Logout</a>')
def index(request):
    return render(request,'demo/index.html')

@login_required
def secure(request):
    return HttpResponse('Secure page. <a href="/openid/logout">Logout</a>')


# def lms(request):
#     form=UserForm
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return render(request,'demo/page.html')
#     return render(request,'demo/lms.html',{'form':form})

def lms(request):
     return render(request,'demo/lms.html')
#def lms(request):
#     return HttpResponse('lms page. <a href="/demo/page.html"> lmspage </a>')
#
# @login_required
def page(request):
    return render(request,'demo/page.html')
#
# def qis(request):
#     form=UserForm
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return render(request,'demo/qispage.html')
#     return render(request,'demo/qis.html',{'form':form})
@login_required
def qispage(request):
    return render(request,'demo/qispage.html')

#upload file
@login_required
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'demo/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'demo/upload.html')