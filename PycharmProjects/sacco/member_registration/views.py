from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'profile.html')
def about(request):
    return render(request, 'about.html')
def member_list(request):
    return render(request, 'member_list.html')
def member_details(request):
    return render(request, 'member_details.html')
