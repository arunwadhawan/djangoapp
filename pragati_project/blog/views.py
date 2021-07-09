from django.shortcuts import render
from django.http import HttpResponse

posts = [{'author':'Piysuh Wadhawan',
          'title':'Blog post 1',
          'content':'First Post Content',
          'date_posted':'July 1, 2021'},
         {'author':'Ridhi Wadhawan',
          'title':'Blog post 2',
          'content':'Second Post Content',
          'date_posted':'July 7, 2021'}
    ]

# Create your views here.

def home(request):
    context = {
        'posts':posts
        }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
