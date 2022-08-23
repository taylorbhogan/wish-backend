from django.http import HttpResponse

from .models import User, Group, Gift

def index(request):
    return HttpResponse("Hello, world.")

def find_wishlists(request):
    userGroups = User.objects.get(id=1).groups.all()
    users = User.objects.filter(groups__in=userGroups)
    print("users-------------->",users)
    if users:
        return HttpResponse(users)
    else:
        return HttpResponse("No users found yet")

def find_gifts(request, user_id):
    gifts = Gift.objects.filter(wished_by=user_id)
    if gifts:
        return HttpResponse([gift.to_dict() for gift in gifts])
    else:
        return HttpResponse("No gifts found yet")
