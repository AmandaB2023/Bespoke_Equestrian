from django.shortcuts import render

# Create your views here.
def about(request):
    """Render about page"""
    return render(request, 'about/about.html')

