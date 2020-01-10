from django.shortcuts import render


def index(request):
    return render(request, 'user/index.html')



def login_user(request):
    pass