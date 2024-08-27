from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'WA_National_Parks/index.html')
