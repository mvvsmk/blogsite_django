from django.shortcuts import render


posts = [
    {
      'author': 'Moturu' ,
       'title':'Blog Post 1',
       'content': 'First post content',
       'date_posted': 'August 04, 2020'
    },
    {
        'author': 'Polly' ,
        'title':'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2018'
    },
]

# Create your views here.



def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title' : "About"})
