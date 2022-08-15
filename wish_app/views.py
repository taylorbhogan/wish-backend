from django.http import HttpResponse

from .models import User, Group, Gift

def index(request):
    return HttpResponse("Hello, world.")

def find_wishlists(request):
    userGroups = User.objects.get(id=1).groups.all()
    users = User.objects.filter(groups__in=userGroups)
    if users:
        return HttpResponse(users)
    else:
        return HttpResponse("No users found yet")
