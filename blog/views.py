from django.shortcuts import render

posts=[
    {
        'author': 'Vijaya',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted': 6-16-2025

    },
    
    {   
        'author': 'Manoj',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 6-16-2025
    }
]

def home(request):
    context = { 
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})