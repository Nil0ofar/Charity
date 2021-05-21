from django.shortcuts import render
from accounts.models import User

def about_us(request):
    if request.method == 'GET':
        users = User.objects.all()
        context = {'users' : users,}
        return render(request, 'about_us.html', context= context)