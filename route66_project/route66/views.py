from django.http import HttpResponse


def mycity(request):
    return HttpResponse("Memphis All Day!")


def myeats(request):
    return HttpResponse("Moe's")
