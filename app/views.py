from django.shortcuts import render

def render_homepage(request):
    return render(request, 'homepage.html')

def render_about(request):
    return render(request, 'about.html')
