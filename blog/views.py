from django.shortcuts import render

posts =[ 
    {
    'author' : 'Kay',
    'title'  : 'Blog Post 1',
    'content': 'First Post content',
    'date_posted' : '14 January 2020'
    },
    {
    'author' : 'Sam',
    'title'  : 'Blog Post 2',
    'content': 'Second Post content',
    'date_posted' : '15 January 2020'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
