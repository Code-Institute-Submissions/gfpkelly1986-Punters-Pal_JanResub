from django.shortcuts import render


# Create your views here.
def get_landing_page(request):
    return render(request, '/workspace/Punters-Pal/templates/index.html')