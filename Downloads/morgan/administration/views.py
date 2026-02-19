from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def portfoliodetails(request):
    return render(request, 'portfolio.html')
def servicesdetails(request):
    return render(request, 'servicesdetails.html')
def starter_page(request):
    return render(request, 'starterpage.html')