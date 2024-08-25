from django.shortcuts import render
def index(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/dashboard.html', {})
    return render(request, "mysite/index.html")