from django.shortcuts import render



# Create your views here.
def index(request):
    # return render_to_response('index.html')
    return render(request, 'index.html')

def index1(request):
    # return render_to_response('index.html')
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contact.html')

def article1(request):
    return render(request, 'article1.html')

def article2(request):
    return render(request, 'article2.html')

def post(request):
    return render(request, 'post.html')

def base(request):
    return render(request, 'base.html')

def social(request):
    return render(request, 'social.html')


def about(request):
    return render(request, 'about.html')

def event(request):

    return render(request, 'event.html')

def edu_info(request):
    return render(request, 'eduinfo.html')


def project(request):
    return render(request, 'project.html')
