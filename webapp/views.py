from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import UserAccount


def index(request):
    users = UserAccount.objects.order_by('-id')
    context = {'users': users}
    return render(request, 'webapp/index.html', context)


def user_info(request, user_id):
    try:
        users = UserAccount.objects.get(pk=user_id)
        user_data = [users.name, users.username, users.email]
    except UserAccount.DoesNotExist:
        raise Http404("User does not exist!")
    return render(request, 'webapp/user_info.html', {'user_title': users, 'user_data': user_data})
