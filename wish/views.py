from django.http import JsonResponse

def ping(request):
    data = {'ping': 'pang!'}
    return JsonResponse(data)
