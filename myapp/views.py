from django.shortcuts import render

# landing page view
def landingPage(request):
    context = {}
    return render(request, 'myapp/landingPage.html', context)

# about page view
def aboutPage(request):
    context = {}
    return render(request, 'myapp/about.html', context)